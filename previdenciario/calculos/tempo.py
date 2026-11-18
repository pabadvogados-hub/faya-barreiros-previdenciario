"""
tempo.py - Tempo de contribuição, conversão de tempo especial e carência (RGPS).

O QUE FAZ
---------
A partir de uma lista de períodos {inicio, fim, tipo} e do sexo do segurado:
  * une as sobreposições: dia concomitante conta UMA vez só para tempo;
  * quando há concomitância entre períodos de tipos diferentes, o dia vale pelo
    MAIOR fator (ex.: dia especial25 concomitante com comum vale 1,40 p/ homem);
  * converte tempo especial em comum (Decreto 3.048/99, art. 70) SOMENTE para
    dias até 13/11/2019 (EC 103/2019, art. 25, §2º: "vedada a conversão para o
    tempo cumprido após esta data");
  * conta a carência em competências (meses) com contribuição;
  * separa o tempo de efetivo magistério (tipo "professor").

TIPOS DE PERÍODO
----------------
  comum       - fator 1,00
  especial25  - homem 1,40 / mulher 1,20   (Dec. 3.048/99, art. 70)
  especial20  - homem 1,75 / mulher 1,50
  especial15  - homem 2,33 / mulher 2,00
  professor   - fator 1,00; conta também como tempo de magistério (não se
                converte magistério em comum desde a EC 18/81)
  rural       - segurado especial: conta como TEMPO até 31/10/1991 sem
                contribuição (Lei 8.213/91, art. 55, §2º), mas NÃO conta para
                carência; depois de 31/10/1991 só conta (tempo e carência) se
                "com_contribuicao": true (art. 39, II).  [CONFERIR]

CONVENÇÃO DE CONTAGEM (parametrizável em `Convencao`)
-----------------------------------------------------
  * Os dias são contados corridos, com início e fim inclusivos
    (01/01/2020 a 31/01/2020 = 31 dias).
  * Para exprimir em anos/meses/dias: ano = 365 dias, mês = 30 dias
    (padrão `Convencao(dias_ano=365, dias_mes=30)`):
        anos  = dias // 365
        meses = (dias % 365) // 30
        dias  = (dias % 365) % 30
    Consequência conhecida: restos de 360 a 364 dias aparecem como "12 meses e
    N dias" (não chegam a 1 ano de 365). Os requisitos ("35 anos") são
    comparados em dias: 35 x 365 = 12.775 dias.
  * O CNIS/INSS costuma decompor cada vínculo por calendário (data a data) e
    somar em base 30/360; o resultado pode diferir em alguns dias.  [CONFERIR]
  * Dias fracionários gerados pela conversão (ex.: 100 x 1,4 = 140,0;
    7 x 2,33 = 16,31) são mantidos com fração nos cálculos internos e
    TRUNCADOS na exibição em anos/meses/dias.  [CONFERIR]

CARÊNCIA
--------
  Cada competência (mês/ano) com ao menos um dia coberto por período que conta
  para carência vale 1 contribuição, contada uma vez só mesmo com vínculos
  concomitantes (Lei 8.213/91, art. 24). Competências informadas em
  "competencias_sem_contribuicao" (ex.: contribuinte individual que não
  recolheu "2015-03") NÃO contam nem para carência nem para tempo naquele
  período. O acréscimo da conversão de especial NÃO conta para carência.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, timedelta

DATA_EC103 = date(2019, 11, 13)          # entrada em vigor da EC 103/2019
DATA_LIMITE_RURAL = date(1991, 10, 31)   # rural sem contribuição conta tempo até aqui

TIPOS_VALIDOS = ("comum", "especial25", "especial20", "especial15", "professor", "rural")

# Decreto 3.048/99, art. 70 (tabela de conversão para tempo comum)
FATORES_CONVERSAO = {
    "M": {"especial25": 1.40, "especial20": 1.75, "especial15": 2.33},
    "F": {"especial25": 1.20, "especial20": 1.50, "especial15": 2.00},
}


@dataclass(frozen=True)
class Convencao:
    """Como transformar dias em anos/meses/dias. Padrão: ano 365, mês 30."""
    dias_ano: int = 365
    dias_mes: int = 30


CONVENCAO_PADRAO = Convencao()


def para_data(valor) -> date:
    """Aceita date ou texto ISO (AAAA-MM-DD) ou brasileiro (DD/MM/AAAA)."""
    if isinstance(valor, date):
        return valor
    texto = str(valor).strip()
    if "/" in texto:
        d, m, a = texto.split("/")
        return date(int(a), int(m), int(d))
    return date.fromisoformat(texto)


def normalizar_sexo(sexo: str) -> str:
    s = str(sexo).strip().upper()[:1]
    if s in ("M", "H"):
        return "M"
    if s == "F":
        return "F"
    raise ValueError(f"Sexo inválido: {sexo!r} (use 'M' ou 'F')")


def fator_conversao(tipo: str, sexo: str) -> float:
    """Fator de conversão especial -> comum (Dec. 3.048/99, art. 70). Comum = 1,0."""
    return FATORES_CONVERSAO[normalizar_sexo(sexo)].get(tipo, 1.0)


def chave_competencia(d: date) -> tuple[int, int]:
    return (d.year, d.month)


def _parse_competencia(texto: str) -> tuple[int, int]:
    """'2015-03' ou '03/2015' -> (2015, 3)."""
    t = str(texto).strip()
    if "/" in t:
        m, a = t.split("/")
    else:
        a, m = t.split("-")[:2]
    return (int(a), int(m))


@dataclass
class Periodo:
    inicio: date
    fim: date
    tipo: str = "comum"
    descricao: str = ""
    competencias_sem_contribuicao: list = field(default_factory=list)
    com_contribuicao: bool = False   # só relevante para "rural"
    conta_carencia: bool | None = None  # None = regra padrão do tipo

    def __post_init__(self):
        self.inicio = para_data(self.inicio)
        self.fim = para_data(self.fim)
        if self.tipo not in TIPOS_VALIDOS:
            raise ValueError(f"Tipo de período inválido: {self.tipo!r}. Válidos: {TIPOS_VALIDOS}")
        if self.fim < self.inicio:
            raise ValueError(f"Período com fim ({self.fim}) antes do início ({self.inicio})")
        self._excluidas = {_parse_competencia(c) for c in self.competencias_sem_contribuicao}

    @classmethod
    def de_dict(cls, d: dict) -> "Periodo":
        return cls(
            inicio=d["inicio"], fim=d["fim"], tipo=d.get("tipo", "comum"),
            descricao=d.get("descricao", ""),
            competencias_sem_contribuicao=list(d.get("competencias_sem_contribuicao", [])),
            com_contribuicao=bool(d.get("com_contribuicao", False)),
            conta_carencia=d.get("conta_carencia"),
        )

    @property
    def dias_corridos(self) -> int:
        return (self.fim - self.inicio).days + 1

    def dia_conta_tempo(self, dia: date) -> bool:
        if chave_competencia(dia) in self._excluidas:
            return False
        if self.tipo == "rural" and not self.com_contribuicao:
            return dia <= DATA_LIMITE_RURAL
        return True

    def dia_conta_carencia(self, dia: date) -> bool:
        if chave_competencia(dia) in self._excluidas:
            return False
        if self.conta_carencia is not None:
            return self.conta_carencia
        if self.tipo == "rural":
            return self.com_contribuicao
        return True


# ---------------------------------------------------------------------------
# Conversões de dias
# ---------------------------------------------------------------------------
def dias_para_amd(dias: float, conv: Convencao = CONVENCAO_PADRAO) -> tuple[int, int, int]:
    """Dias (truncados) -> (anos, meses, dias) pela convenção."""
    total = int(dias)
    anos, resto = divmod(total, conv.dias_ano)
    meses, d = divmod(resto, conv.dias_mes)
    return anos, meses, d


def amd_para_dias(anos: int = 0, meses: int = 0, dias: int = 0,
                  conv: Convencao = CONVENCAO_PADRAO) -> int:
    return anos * conv.dias_ano + meses * conv.dias_mes + dias


def anos_em_dias(anos: float, conv: Convencao = CONVENCAO_PADRAO) -> float:
    return anos * conv.dias_ano


def formatar_amd(dias: float, conv: Convencao = CONVENCAO_PADRAO) -> str:
    if dias < 0:
        return "-" + formatar_amd(-dias, conv)
    a, m, d = dias_para_amd(dias, conv)
    return f"{a}a {m}m {d}d"


def unir_periodos(intervalos) -> list[tuple[date, date]]:
    """Une intervalos [inicio, fim] sobrepostos ou contíguos."""
    pares = sorted((para_data(i), para_data(f)) for i, f in intervalos)
    unidos: list[list[date]] = []
    for ini, fim in pares:
        if unidos and ini <= unidos[-1][1] + timedelta(days=1):
            if fim > unidos[-1][1]:
                unidos[-1][1] = fim
        else:
            unidos.append([ini, fim])
    return [(a, b) for a, b in unidos]


# ---------------------------------------------------------------------------
# Linha do tempo dia a dia (base de todos os cálculos)
# ---------------------------------------------------------------------------
class LinhaDoTempo:
    """
    Monta, dia a dia, o que cada dia vale e guarda somas acumuladas para
    consultas rápidas "até a data X" (usadas na projeção das regras).
    """

    def __init__(self, periodos: list[Periodo], sexo: str):
        self.sexo = normalizar_sexo(sexo)
        self.periodos = sorted(periodos, key=lambda p: (p.inicio, p.fim))
        if not self.periodos:
            self.inicio = self.fim = None
            return
        self.inicio = min(p.inicio for p in self.periodos)
        self.fim = max(p.fim for p in self.periodos)
        n = (self.fim - self.inicio).days + 1

        # fator em CENTÉSIMOS inteiros (1,40 -> 140): soma exata, sem erro de ponto flutuante
        fator = [0] * n            # 0 = dia não conta como tempo
        magist = [False] * n
        carencia_dia = [False] * n
        for p in self.periodos:
            f_especial = round(fator_conversao(p.tipo, self.sexo) * 100)
            off = (p.inicio - self.inicio).days
            dia = p.inicio
            for i in range(off, off + p.dias_corridos):
                if p.dia_conta_tempo(dia):
                    f = f_especial if dia <= DATA_EC103 else 100
                    if f > fator[i]:
                        fator[i] = f
                    if p.tipo == "professor":
                        magist[i] = True
                if p.dia_conta_carencia(dia):
                    carencia_dia[i] = True
                dia += timedelta(days=1)

        # acumulados (índice i = soma até o dia inicio+i, inclusive)
        self._bruto, self._conv, self._mag, self._car = [], [], [], []
        sb = sc = sm = 0
        scar = 0
        vistas: set = set()
        self._competencias: list[tuple[int, int]] = []
        dia = self.inicio
        for i in range(n):
            if fator[i] > 0:
                sb += 1
                sc += fator[i]
            if magist[i]:
                sm += 1
            if carencia_dia[i]:
                k = chave_competencia(dia)
                if k not in vistas:
                    vistas.add(k)
                    scar += 1
                    self._competencias.append(k)
            self._bruto.append(sb)
            self._conv.append(sc)
            self._mag.append(sm)
            self._car.append(scar)
            dia += timedelta(days=1)
        self._carencia_dia = carencia_dia

    # --- consulta acumulada ---
    def _idx(self, ate: date | None) -> int:
        if self.inicio is None:
            return -1
        if ate is None:
            return len(self._bruto) - 1
        ate = para_data(ate)
        if ate < self.inicio:
            return -1
        return min((ate - self.inicio).days, len(self._bruto) - 1)

    def _get(self, arr, ate) -> float:
        i = self._idx(ate)
        return arr[i] if i >= 0 else 0

    def tempo_bruto(self, ate: date | None = None) -> int:
        """Dias com contribuição (união, sem conversão) até a data, inclusive."""
        return int(self._get(self._bruto, ate)) if self.inicio else 0

    def tempo_contribuicao(self, ate: date | None = None) -> float:
        """Dias de tempo de contribuição COM conversão do especial até 13/11/2019."""
        return self._get(self._conv, ate) / 100 if self.inicio else 0.0

    def acrescimo_conversao(self, ate: date | None = None) -> float:
        return self.tempo_contribuicao(ate) - self.tempo_bruto(ate)

    def tempo_magisterio(self, ate: date | None = None) -> int:
        return int(self._get(self._mag, ate)) if self.inicio else 0

    def carencia(self, ate: date | None = None) -> int:
        """Número de competências (meses) com contribuição até a data."""
        return int(self._get(self._car, ate)) if self.inicio else 0

    def competencias(self) -> list[tuple[int, int]]:
        return list(self._competencias) if self.inicio else []

    def intervalos_contribuicao(self) -> list[tuple[date, date]]:
        """Intervalos contínuos de dias que contam para carência (p/ qualidade de segurado)."""
        if self.inicio is None:
            return []
        res = []
        ini = None
        for i, ok in enumerate(self._carencia_dia):
            d = self.inicio + timedelta(days=i)
            if ok and ini is None:
                ini = d
            elif not ok and ini is not None:
                res.append((ini, d - timedelta(days=1)))
                ini = None
        if ini is not None:
            res.append((ini, self.fim))
        return res


# ---------------------------------------------------------------------------
# Resumo para relatório
# ---------------------------------------------------------------------------
def calcular_tempo(periodos: list[Periodo], sexo: str, ate: date | None = None,
                   conv: Convencao = CONVENCAO_PADRAO) -> dict:
    """Resumo completo do tempo até a data `ate` (ou até o fim do último período)."""
    sexo = normalizar_sexo(sexo)
    lt = LinhaDoTempo(periodos, sexo)
    ate = para_data(ate) if ate else lt.fim

    linhas = []
    for p in sorted(periodos, key=lambda x: (x.inicio, x.fim)):
        fim_ef = min(p.fim, ate) if ate else p.fim
        if ate and p.inicio > ate:
            continue
        dias = sum(1 for k in range((fim_ef - p.inicio).days + 1)
                   if p.dia_conta_tempo(p.inicio + timedelta(days=k)))
        f = fator_conversao(p.tipo, sexo)
        ate_ec = 0
        if p.inicio <= DATA_EC103:
            lim = min(fim_ef, DATA_EC103)
            ate_ec = sum(1 for k in range((lim - p.inicio).days + 1)
                         if p.dia_conta_tempo(p.inicio + timedelta(days=k)))
        convertido = ate_ec * f + (dias - ate_ec)
        concomitante = any(
            q is not p and q.inicio <= fim_ef and p.inicio <= q.fim for q in periodos
        )
        linhas.append({
            "inicio": p.inicio, "fim": fim_ef, "tipo": p.tipo, "descricao": p.descricao,
            "dias": dias, "fator": f, "dias_convertidos": convertido,
            "concomitante": concomitante,
        })

    return {
        "ate": ate,
        "periodos": linhas,
        "tempo_bruto_dias": lt.tempo_bruto(ate),
        "acrescimo_conversao_dias": lt.acrescimo_conversao(ate),
        "tempo_contribuicao_dias": lt.tempo_contribuicao(ate),
        "tempo_ate_ec103_dias": lt.tempo_contribuicao(min(ate, DATA_EC103)) if ate else 0,
        "tempo_magisterio_dias": lt.tempo_magisterio(ate),
        "carencia_meses": lt.carencia(ate),
        "convencao": conv,
        "linha": lt,
    }
