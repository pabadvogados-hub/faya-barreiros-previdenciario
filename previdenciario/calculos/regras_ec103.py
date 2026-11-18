"""
regras_ec103.py - Simulador das regras de aposentadoria do RGPS (EC 103/2019).

Para cada regra devolve: aplicável?, cumpre na data-base?, data em que cumpre
(com ou sem projeção de contribuição contínua a partir da data-base),
requisitos faltantes na data-base e o COEFICIENTE da RMI (não calcula o valor:
isso exige os salários de contribuição).

Abreviações: M = mulher, H = homem. "Tempo" = tempo de contribuição, com a
conversão do especial até 13/11/2019 (ver tempo.py). Carência mínima de 180
contribuições (Lei 8.213/91, art. 25, II) é exigida em todas as regras.
O requisito que varia por ano é o do ANO CIVIL da data em que o último
requisito é cumprido (EC 103, art. 15, §1º; art. 16, §1º; art. 18, §1º).

DIREITO ADQUIRIDO ATÉ 13/11/2019 (EC 103, art. 3º)
  DA-TC  Aposentadoria por tempo de contribuição (Lei 8.213/91, art. 52/53 e
         art. 29, I, com a redação da Lei 9.876/99): 30 M / 35 H, sem idade
         mínima. Coeficiente 100% x FATOR PREVIDENCIÁRIO.
         Professor (CF art. 201, §8º, redação anterior): 25 M / 30 H de
         magistério; fator com bônus de 5/10 anos (Lei 8.213/91, art. 29, §9º).
  DA-PT  Regra de pontos sem fator (Lei 8.213/91, art. 29-C, incluído pela
         Lei 13.183/2015): tempo 30 M / 35 H e idade + tempo >= 85 M / 95 H
         até 30/12/2018 e 86 M / 96 H a partir de 31/12/2018 (art. 29-C, §2º,
         I). Vigência desde 18/06/2015 (MP 676/2015). Coeficiente 100% SEM fator
         (o fator só se aplica se for mais vantajoso).
         Professor (art. 29-C, §3º): tempo 25 M / 30 H de magistério e +5
         pontos sobre a soma.

TRANSIÇÃO - SÓ PARA QUEM ERA FILIADO ATÉ 13/11/2019
  Art. 15  Pontos: tempo 30 M / 35 H e idade + tempo >= 86 M / 96 H em 2019,
           +1 ponto a cada 1º de janeiro a partir de 2020, até 100 M (2033) e
           105 H (2028). Professor (§3º): tempo 25 M / 30 H de magistério,
           81 M / 91 H, +1 por ano até 92 M (2030) e 100 H (2028).
           Coeficiente: art. 26, §2º, I (60% + 2%/ano).
  Art. 16  Idade mínima progressiva: tempo 30 M / 35 H e idade 56 M / 61 H em
           2019, +6 meses a cada ano a partir de 2020, até 62 M (2031) e
           65 H (2027). Professor (§2º): menos 5 anos em tempo e idade -
           25 M / 30 H; 51 M / 56 H, +6 meses/ano até 57 M (2031) e 60 H
           (2027). Coeficiente: art. 26, §2º, I.
  Art. 17  Pedágio 50%: SÓ para quem tinha MAIS DE 28 M / 33 H anos de
           contribuição em 13/11/2019. Tempo 30 M / 35 H + 50% do tempo que
           faltava em 13/11/2019. Sem idade mínima. RMI = média x FATOR
           PREVIDENCIÁRIO (art. 17, parágrafo único) -> coeficiente 100% x FP.
  Art. 20  Pedágio 100%: idade 57 M / 60 H; tempo 30 M / 35 H + 100% do
           tempo que faltava em 13/11/2019. Professor (§1º): menos 5 anos em
           idade e tempo (52 M / 55 H; 25 M / 30 H de magistério). Coeficiente
           100% (art. 26, §3º, I).
  Art. 18  Idade (transição): 60 M / 65 H; 15 anos de contribuição (ambos os
           sexos). Para a mulher, +6 meses por ano a partir de 2020 até 62
           (2023) (art. 18, §1º). Coeficiente: art. 26, §2º, I.

PERMANENTE
  Art. 19  62 M / 65 H; tempo 15 M / 20 H. Para o homem filiado ATÉ
           13/11/2019, o tempo exigido é 15 anos (art. 18). Professor
           (art. 19, §1º, II): 57 M / 60 H com 25 anos de magistério.
           Coeficiente: art. 26, §2º, IV.

COEFICIENTE (EC 103, art. 26)
  §2º: 60% + 2 pontos percentuais por ano de contribuição que exceder 20 anos;
  §5º: para MULHERES (e art. 19, §1º, I, "a"), o acréscimo conta a partir de
  15 anos. §3º: 100% no art. 20 (pedágio 100%) e na incapacidade acidentária.
  Anos excedentes = anos COMPLETOS de tempo de contribuição.

PONTOS CONTROVERTIDOS (marcados, não decididos em silêncio)
  [CONFERIR] Frações nos pontos: padrão "amd" soma idade (calendário) e tempo
             em anos/meses/dias e normaliza em base 30/360 (método usual do
             INSS); alternativa "decimal" (dias/365,25 + tempo/365).
             Efeito conhecido do "amd": idade com resto de 30 dias (mês de 31
             dias, ex.: 69a 11m 30d) vira +1 mês na normalização, e os pontos
             podem fechar UM DIA antes do aniversário (ver teste do art. 15).
  [CONFERIR] Professor: pontos com idade + tempo de MAGISTÉRIO (padrão) ou
             idade + tempo TOTAL de contribuição (`professor_pontos_tempo`).
  [CONFERIR] Tempo convertido (especial -> comum) contando para os 15/20 anos
             das regras de idade (art. 18/19). Padrão: conta para o tempo, NÃO
             para a carência (`tempo_convertido_nas_regras_idade`).
  [CONFERIR] Homem filiado antes da EC pelo art. 18: o acréscimo de 2% conta
             acima de 20 anos (texto do art. 26, §2º); há tese de que deveria
             contar acima de 15.
  [CONFERIR] Coeficiente acima de 100% não é limitado aqui (o art. 26 não
             limita; a RMI fica sujeita ao teto do RGPS).
  [CONFERIR] Coeficiente informado na data de referência = a mais tardia entre
             a data de cumprimento e a data-base (DER presumida).
"""
from __future__ import annotations

import calendar
from dataclasses import dataclass, field
from datetime import date, timedelta

from tempo import (CONVENCAO_PADRAO, DATA_EC103, Convencao, LinhaDoTempo, Periodo,
                   dias_para_amd, formatar_amd, normalizar_sexo, para_data)

DATA_LEI_13183 = date(2015, 6, 18)    # MP 676/2015 (art. 29-C)
DATA_PONTOS_86_96 = date(2018, 12, 31)
CARENCIA_MINIMA = 180

CONFERIR = [
    "Convenção de contagem: dias corridos com ano de 365 e mês de 30 (o CNIS decompõe por calendário em base 30/360).",
    "Dias fracionários da conversão especial->comum: mantidos no cálculo e truncados na exibição.",
    "Tempo rural: até 31/10/1991 conta tempo sem carência; depois só com contribuição.",
    "Frações nos pontos: soma de anos/meses/dias em base 30/360 (padrão) x decimal; no padrão, idade com resto de 30 dias normaliza e os pontos podem fechar 1 dia antes do aniversário.",
    "Professor: pontos com tempo de magistério (padrão) x tempo total.",
    "Tempo convertido contando para os 15/20 anos das regras de idade (art. 18/19); não conta para carência.",
    "Homem filiado antes da EC (art. 18): acréscimo de 2% acima de 20 anos (texto) x acima de 15 (tese).",
    "Coeficiente acima de 100% não limitado (RMI limitada ao teto).",
    "Coeficiente apurado na data mais tardia entre cumprimento e data-base.",
    "Período de graça: 'mais de 120' = 121+ (padrão) x 120; prorrogação de 24 meses adquirida uma vez se mantém (TNU, padrão) x só na sequência atual.",
    "Período de graça: desemprego não é considerado ao apurar perdas passadas do histórico.",
]


# ---------------------------------------------------------------------------
# Datas e idade
# ---------------------------------------------------------------------------
def somar_meses_data(d: date, n: int) -> date:
    """Soma n meses a uma data. Se o dia não existir no mês final, vence no
    1º dia do mês seguinte (Código Civil, art. 132, §3º) - ex.: 29/02 + 12m."""
    total = d.year * 12 + (d.month - 1) + n
    a, m = total // 12, total % 12 + 1
    ultimo = calendar.monthrange(a, m)[1]
    if d.day <= ultimo:
        return date(a, m, d.day)
    return date(a, m, ultimo) + timedelta(days=1)


def idade_meses(nascimento: date, d: date) -> tuple[int, int]:
    """(meses completos de idade, dias além disso) na data d."""
    k = (d.year - nascimento.year) * 12 + (d.month - nascimento.month) + 1
    while k > 0 and somar_meses_data(nascimento, k) > d:
        k -= 1
    return k, (d - somar_meses_data(nascimento, k)).days


def idade_amd(nascimento: date, d: date) -> tuple[int, int, int]:
    k, dias = idade_meses(nascimento, d)
    return k // 12, k % 12, dias


def fmt_meses(m: int) -> str:
    return f"{m // 12}a {m % 12}m"


# ---------------------------------------------------------------------------
# Tabelas progressivas (conferidas com o texto da EC 103/2019 no planalto.gov.br)
# ---------------------------------------------------------------------------
def _anos_desde_2019(ano: int) -> int:
    return max(0, ano - 2019)


def pontos_art15(sexo: str, ano: int, professor: bool = False) -> int:
    if professor:
        ini, teto = (81, 92) if sexo == "F" else (91, 100)
    else:
        ini, teto = (86, 100) if sexo == "F" else (96, 105)
    return min(ini + _anos_desde_2019(ano), teto)


def idade_art16_meses(sexo: str, ano: int, professor: bool = False) -> int:
    if professor:
        ini, teto = (51, 57) if sexo == "F" else (56, 60)
    else:
        ini, teto = (56, 62) if sexo == "F" else (61, 65)
    return min(ini * 12 + 6 * _anos_desde_2019(ano), teto * 12)


def idade_art18_meses(sexo: str, ano: int) -> int:
    if sexo == "M":
        return 65 * 12
    return min(60 * 12 + 6 * _anos_desde_2019(ano), 62 * 12)


def coeficiente_art26(tempo_dias: float, sexo: str, conv: Convencao = CONVENCAO_PADRAO,
                      limiar_homem: int = 20) -> float:
    anos = int(tempo_dias // conv.dias_ano)
    limiar = 15 if sexo == "F" else limiar_homem
    return round(0.60 + 0.02 * max(0, anos - limiar), 4)


# ---------------------------------------------------------------------------
# Estruturas
# ---------------------------------------------------------------------------
@dataclass
class Segurado:
    nascimento: date
    sexo: str
    nome: str = ""

    def __post_init__(self):
        self.nascimento = para_data(self.nascimento)
        self.sexo = normalizar_sexo(self.sexo)


@dataclass
class Opcoes:
    convencao: Convencao = CONVENCAO_PADRAO
    metodo_pontos: str = "amd"                   # "amd" | "decimal"   [CONFERIR]
    professor_pontos_tempo: str = "magisterio"   # "magisterio" | "total" [CONFERIR]
    tempo_convertido_nas_regras_idade: bool = True  # [CONFERIR]
    horizonte_anos: int = 45                     # até quando procurar a data


@dataclass
class ResultadoRegra:
    codigo: str
    nome: str
    fundamento: str
    aplicavel: bool = True
    motivo_inaplicavel: str = ""
    cumpre: bool = False                 # cumpre na data-base
    data_cumprimento: date | None = None
    faltantes: list = field(default_factory=list)
    coeficiente: float | None = None
    com_fator: bool = False
    observacoes: list = field(default_factory=list)


class _Contexto:
    def __init__(self, lt: LinhaDoTempo, seg: Segurado, op: Opcoes):
        self.lt, self.seg, self.op, self.conv = lt, seg, op, op.convencao

    def tempo(self, d: date, fonte: str) -> float:
        if fonte == "mag":
            return self.lt.tempo_magisterio(d)
        if fonte == "bruto":
            return self.lt.tempo_bruto(d)
        return self.lt.tempo_contribuicao(d)

    def pontos_ok(self, d: date, pontos: int, fonte: str, bonus: int = 0) -> bool:
        return self.pontos_unidades(d, fonte, bonus) >= self.pontos_exigidos_unidades(pontos)

    def pontos_exigidos_unidades(self, pontos: int) -> float:
        return pontos * (360 if self.op.metodo_pontos == "amd" else 1)

    def pontos_unidades(self, d: date, fonte: str, bonus: int = 0) -> float:
        t = self.tempo(d, fonte)
        if self.op.metodo_pontos == "decimal":
            return (d - self.seg.nascimento).days / 365.25 + t / self.conv.dias_ano + bonus
        ia, im, idd = idade_amd(self.seg.nascimento, d)
        ta, tm, td = dias_para_amd(t, self.conv)
        return (ia + ta + bonus) * 360 + (im + tm) * 30 + (idd + td)

    def fmt_pontos(self, d: date, fonte: str, bonus: int = 0) -> str:
        u = self.pontos_unidades(d, fonte, bonus)
        if self.op.metodo_pontos == "decimal":
            return f"{u:.2f}"
        u = int(u)
        return f"{u // 360}a {(u % 360) // 30}m {u % 30}d"


# Um requisito = (verificação(d) -> bool, descrição(d) -> str)
def _req_tempo(ctx, exigido, fonte, rotulo):
    nomes = {"tc": "tempo de contribuição", "mag": "tempo de magistério", "bruto": "tempo (sem conversão)"}
    def ok(d):
        return ctx.tempo(d, fonte) + 1e-9 >= exigido
    def txt(d):
        atual = ctx.tempo(d, fonte)
        return (f"{nomes[fonte]}: exigido {formatar_amd(exigido, ctx.conv)}{rotulo}, "
                f"atual {formatar_amd(atual, ctx.conv)}, faltam {formatar_amd(exigido - atual, ctx.conv)}")
    return ok, txt


def _req_idade(ctx, exig_meses_fn):
    def ok(d):
        return idade_meses(ctx.seg.nascimento, d)[0] >= exig_meses_fn(d)
    def txt(d):
        a, m, dd = idade_amd(ctx.seg.nascimento, d)
        return f"idade: exigida {fmt_meses(exig_meses_fn(d))} (em {d.year}), atual {a}a {m}m {dd}d"
    return ok, txt


def _req_pontos(ctx, pontos_fn, fonte, bonus=0):
    def ok(d):
        return ctx.pontos_ok(d, pontos_fn(d), fonte, bonus)
    def txt(d):
        extra = f" (inclui bônus de {bonus})" if bonus else ""
        return f"pontos: exigidos {pontos_fn(d)} (em {d.year}), atuais {ctx.fmt_pontos(d, fonte, bonus)}{extra}"
    return ok, txt


def _req_carencia(ctx, minimo=CARENCIA_MINIMA):
    def ok(d):
        return ctx.lt.carencia(d) >= minimo
    def txt(d):
        return f"carência: exigidas {minimo} contribuições, atuais {ctx.lt.carencia(d)}"
    return ok, txt


def _buscar(requisitos, inicio: date, fim: date) -> date | None:
    d = inicio
    um = timedelta(days=1)
    while d <= fim:
        if all(ok(d) for ok, _ in requisitos):
            return d
        d += um
    return None


def _faltantes(requisitos, d: date) -> list[str]:
    return [txt(d) for ok, txt in requisitos if not ok(d)]


# ---------------------------------------------------------------------------
# Simulação
# ---------------------------------------------------------------------------
def simular_regras(periodos: list[Periodo], segurado: Segurado, data_base: date,
                   projetar: bool = False, opcoes: Opcoes | None = None) -> list[ResultadoRegra]:
    op = opcoes or Opcoes()
    conv = op.convencao
    data_base = para_data(data_base)
    sexo = segurado.sexo
    F = sexo == "F"

    periodos_calc = list(periodos)
    horizonte = somar_meses_data(data_base, 12 * op.horizonte_anos)
    if projetar:
        periodos_calc.append(Periodo(data_base + timedelta(days=1), horizonte, "comum",
                                     "Projeção de contribuição contínua"))
    lt = LinhaDoTempo(periodos_calc, sexo)
    ctx = _Contexto(lt, segurado, op)
    if lt.inicio is None:
        return []

    inicio = lt.inicio
    filiado_antes = min(p.inicio for p in periodos) <= DATA_EC103
    tem_magisterio = any(p.tipo == "professor" for p in periodos)
    anos = lambda n: n * conv.dias_ano
    fonte_idade = "tc" if op.tempo_convertido_nas_regras_idade else "bruto"
    fonte_pontos_prof = "mag" if op.professor_pontos_tempo == "magisterio" else "tc"
    tc2019 = lt.tempo_contribuicao(DATA_EC103)
    mag2019 = lt.tempo_magisterio(DATA_EC103)
    ini_ec = max(inicio, DATA_EC103)
    base_tc = anos(30 if F else 35)
    base_mag = anos(25 if F else 30)

    resultados: list[ResultadoRegra] = []

    def coef_art26_em(d, limiar_homem=20):
        return coeficiente_art26(lt.tempo_contribuicao(d), sexo, conv, limiar_homem)

    def registrar(res: ResultadoRegra, reqs, ini: date, fim: date, coef_fn=None,
                  ref_faltantes: date | None = None):
        res.data_cumprimento = _buscar(reqs, ini, fim) if ini <= fim else None
        res.cumpre = res.data_cumprimento is not None and res.data_cumprimento <= data_base
        ref = ref_faltantes or data_base
        res.faltantes = [] if res.cumpre else _faltantes(reqs, ref)
        if res.data_cumprimento is None and not res.faltantes:
            res.faltantes = ["não cumpre dentro da janela da regra"]
        if coef_fn and res.data_cumprimento:
            res.coeficiente = coef_fn(max(res.data_cumprimento, data_base))
        resultados.append(res)

    # --- Direito adquirido até 13/11/2019 -------------------------------
    if inicio <= DATA_EC103:
        ref = min(data_base, DATA_EC103)
        r = ResultadoRegra("DA-TC", "Direito adquirido - tempo de contribuição (com fator)",
                           "EC 103, art. 3º; Lei 8.213/91, arts. 52, 53 e 29, I", com_fator=True,
                           observacoes=["RMI = média x fator previdenciário (FP não calculado aqui)."])
        reqs = [_req_tempo(ctx, base_tc, "tc", ""), _req_carencia(ctx)]
        registrar(r, reqs, inicio, DATA_EC103, lambda d: 1.0, ref)

        r = ResultadoRegra("DA-PT", f"Direito adquirido - pontos {85 if F else 95}/{86 if F else 96} sem fator",
                           "Lei 8.213/91, art. 29-C (Lei 13.183/2015)",
                           observacoes=["85/95 até 30/12/2018; 86/96 de 31/12/2018 a 13/11/2019.",
                                        "100% da média, sem fator (fator só se mais vantajoso)."])
        pts = lambda d: (85 if F else 95) + (1 if d >= DATA_PONTOS_86_96 else 0)
        reqs = [_req_tempo(ctx, base_tc, "tc", ""), _req_pontos(ctx, pts, "tc"), _req_carencia(ctx)]
        registrar(r, reqs, max(inicio, DATA_LEI_13183), DATA_EC103, lambda d: 1.0, ref)

        if tem_magisterio:
            r = ResultadoRegra("DA-TC-P", "Direito adquirido - professor (com fator)",
                               "EC 103, art. 3º; CF art. 201, §8º (redação anterior); Lei 8.213/91, art. 29, §9º",
                               com_fator=True,
                               observacoes=["Fator com bônus de 5 anos (M) / 10 anos (H) no tempo."])
            reqs = [_req_tempo(ctx, base_mag, "mag", ""), _req_carencia(ctx)]
            registrar(r, reqs, inicio, DATA_EC103, lambda d: 1.0, ref)

            r = ResultadoRegra("DA-PT-P", "Direito adquirido - professor pontos sem fator",
                               "Lei 8.213/91, art. 29-C, §3º",
                               observacoes=["Magistério 25 M / 30 H e +5 pontos sobre a soma."])
            reqs = [_req_tempo(ctx, base_mag, "mag", ""),
                    _req_pontos(ctx, pts, fonte_pontos_prof, bonus=5), _req_carencia(ctx)]
            registrar(r, reqs, max(inicio, DATA_LEI_13183), DATA_EC103, lambda d: 1.0, ref)

    # --- Transições (exigem filiação até 13/11/2019) ----------------------
    def inaplicavel(codigo, nome, fundamento, motivo):
        resultados.append(ResultadoRegra(codigo, nome, fundamento, aplicavel=False,
                                         motivo_inaplicavel=motivo))

    nao_filiado = "filiação posterior a 13/11/2019 (só regra permanente)"

    # Art. 15 - pontos
    nome, fund = "Transição por pontos", "EC 103, art. 15"
    if not filiado_antes:
        inaplicavel("ART15", nome, fund, nao_filiado)
    else:
        r = ResultadoRegra("ART15", nome, fund,
                           observacoes=[f"Pontos {86 if F else 96} em 2019, +1/ano até {100 if F else 105}."])
        reqs = [_req_tempo(ctx, base_tc, "tc", ""),
                _req_pontos(ctx, lambda d: pontos_art15(sexo, d.year), "tc"), _req_carencia(ctx)]
        registrar(r, reqs, ini_ec, horizonte, coef_art26_em)
        if tem_magisterio:
            r = ResultadoRegra("ART15-P", nome + " - professor", fund + ", §3º",
                               observacoes=[f"Pontos {81 if F else 91} em 2019, +1/ano até {92 if F else 100}."])
            reqs = [_req_tempo(ctx, base_mag, "mag", ""),
                    _req_pontos(ctx, lambda d: pontos_art15(sexo, d.year, True), fonte_pontos_prof),
                    _req_carencia(ctx)]
            registrar(r, reqs, ini_ec, horizonte, coef_art26_em)

    # Art. 16 - idade mínima progressiva
    nome, fund = "Transição por idade mínima progressiva", "EC 103, art. 16"
    if not filiado_antes:
        inaplicavel("ART16", nome, fund, nao_filiado)
    else:
        r = ResultadoRegra("ART16", nome, fund,
                           observacoes=[f"Idade {56 if F else 61} em 2019, +6 meses/ano até {62 if F else 65}."])
        reqs = [_req_tempo(ctx, base_tc, "tc", ""),
                _req_idade(ctx, lambda d: idade_art16_meses(sexo, d.year)), _req_carencia(ctx)]
        registrar(r, reqs, ini_ec, horizonte, coef_art26_em)
        if tem_magisterio:
            r = ResultadoRegra("ART16-P", nome + " - professor", fund + ", §2º",
                               observacoes=[f"Idade {51 if F else 56} em 2019, +6 meses/ano até {57 if F else 60}."])
            reqs = [_req_tempo(ctx, base_mag, "mag", ""),
                    _req_idade(ctx, lambda d: idade_art16_meses(sexo, d.year, True)), _req_carencia(ctx)]
            registrar(r, reqs, ini_ec, horizonte, coef_art26_em)

    # Art. 17 - pedágio 50%
    nome, fund = "Transição pedágio 50% (sem idade, com fator)", "EC 103, art. 17"
    limite17 = anos(28 if F else 33)
    if not filiado_antes:
        inaplicavel("ART17", nome, fund, nao_filiado)
    elif not tc2019 > limite17:
        inaplicavel("ART17", nome, fund,
                    f"em 13/11/2019 tinha {formatar_amd(tc2019, conv)}; exige MAIS DE "
                    f"{28 if F else 33} anos de contribuição")
    else:
        pedagio = 0.5 * max(0.0, base_tc - tc2019)
        r = ResultadoRegra("ART17", nome, fund, com_fator=True,
                           observacoes=[f"Pedágio: {formatar_amd(pedagio, conv)} (50% do que faltava em 13/11/2019).",
                                        "RMI = média x fator previdenciário (art. 17, parágrafo único)."])
        reqs = [_req_tempo(ctx, base_tc + pedagio, "tc", " (com pedágio)"), _req_carencia(ctx)]
        registrar(r, reqs, ini_ec, horizonte, lambda d: 1.0)

    # Art. 20 - pedágio 100%
    nome, fund = "Transição pedágio 100% (idade mínima)", "EC 103, art. 20"
    if not filiado_antes:
        inaplicavel("ART20", nome, fund, nao_filiado)
    else:
        pedagio = max(0.0, base_tc - tc2019)
        r = ResultadoRegra("ART20", nome, fund,
                           observacoes=[f"Pedágio: {formatar_amd(pedagio, conv)} (100% do que faltava em 13/11/2019).",
                                        "Coeficiente 100% (art. 26, §3º, I)."])
        reqs = [_req_tempo(ctx, base_tc + pedagio, "tc", " (com pedágio)"),
                _req_idade(ctx, lambda d: (57 if F else 60) * 12), _req_carencia(ctx)]
        registrar(r, reqs, ini_ec, horizonte, lambda d: 1.0)
        if tem_magisterio:
            pedagio_p = max(0.0, base_mag - mag2019)
            r = ResultadoRegra("ART20-P", nome + " - professor", fund + ", §1º",
                               observacoes=[f"Pedágio: {formatar_amd(pedagio_p, conv)} de magistério.",
                                            "Coeficiente 100% (art. 26, §3º, I)."])
            reqs = [_req_tempo(ctx, base_mag + pedagio_p, "mag", " (com pedágio)"),
                    _req_idade(ctx, lambda d: (52 if F else 55) * 12), _req_carencia(ctx)]
            registrar(r, reqs, ini_ec, horizonte, lambda d: 1.0)

    # Art. 18 - idade (transição)
    nome, fund = "Transição aposentadoria por idade", "EC 103, art. 18"
    if not filiado_antes:
        inaplicavel("ART18", nome, fund, nao_filiado)
    else:
        r = ResultadoRegra("ART18", nome, fund,
                           observacoes=["Mulher 60 em 2019, +6 meses/ano até 62 (2023); homem 65."])
        reqs = [_req_tempo(ctx, anos(15), fonte_idade, ""),
                _req_idade(ctx, lambda d: idade_art18_meses(sexo, d.year)), _req_carencia(ctx)]
        registrar(r, reqs, ini_ec, horizonte, coef_art26_em)

    # Art. 19 - permanente
    tempo19 = 15 if (F or filiado_antes) else 20
    obs19 = []
    if not F and filiado_antes:
        obs19.append("Homem filiado até 13/11/2019: 15 anos de contribuição (art. 18).")
    r = ResultadoRegra("ART19", "Regra permanente (idade)", "EC 103, art. 19", observacoes=obs19)
    reqs = [_req_tempo(ctx, anos(tempo19), fonte_idade, ""),
            _req_idade(ctx, lambda d: (62 if F else 65) * 12), _req_carencia(ctx)]
    registrar(r, reqs, ini_ec, horizonte, coef_art26_em)
    if tem_magisterio:
        r = ResultadoRegra("ART19-P", "Regra permanente - professor", "EC 103, art. 19, §1º, II")
        reqs = [_req_tempo(ctx, anos(25), "mag", ""),
                _req_idade(ctx, lambda d: (57 if F else 60) * 12), _req_carencia(ctx)]
        registrar(r, reqs, ini_ec, horizonte, coef_art26_em)

    return resultados


def melhores_regras(resultados: list[ResultadoRegra]) -> dict:
    """Melhor regra pela data mais próxima e pelo maior coeficiente."""
    com_data = [r for r in resultados if r.aplicavel and r.data_cumprimento]
    if not com_data:
        return {"por_data": None, "por_coeficiente": None}
    por_data = min(com_data, key=lambda r: (r.data_cumprimento, -(r.coeficiente or 0), r.com_fator))
    sem_fator = [r for r in com_data if not r.com_fator]
    por_coef = (max(sem_fator, key=lambda r: (r.coeficiente or 0, -r.data_cumprimento.toordinal()))
                if sem_fator else None)
    return {"por_data": por_data, "por_coeficiente": por_coef}
