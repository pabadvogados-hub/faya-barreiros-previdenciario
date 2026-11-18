"""
test_calculos.py - Testes dos cálculos previdenciários.

Rodar:  python -m unittest test_calculos -v
"""
import os
import unittest
from datetime import date, timedelta

from periodo_graca import (analisar_qualidade, calcular_periodo_graca,
                           data_perda_qualidade, somar_meses)
from regras_ec103 import (Opcoes, Segurado, coeficiente_art26, idade_amd,
                          idade_art16_meses, idade_art18_meses, pontos_art15,
                          simular_regras, somar_meses_data)
from tempo import (DATA_EC103, LinhaDoTempo, Periodo, calcular_tempo,
                   dias_para_amd, fator_conversao, unir_periodos)

D = date


def periodo_com_dias(fim: date, dias: int, tipo="comum") -> Periodo:
    """Período que termina em `fim` e tem exatamente `dias` dias corridos."""
    return Periodo(fim - timedelta(days=dias - 1), fim, tipo)


def regra(resultados, codigo):
    return next(r for r in resultados if r.codigo == codigo)


# ===========================================================================
# tempo.py
# ===========================================================================
class TestTempo(unittest.TestCase):
    def test_sobreposicao_conta_uma_vez(self):
        ps = [Periodo(D(2000, 1, 1), D(2000, 12, 31)), Periodo(D(2000, 7, 1), D(2001, 6, 30))]
        lt = LinhaDoTempo(ps, "M")
        self.assertEqual(lt.tempo_bruto(), 366 + 181)  # 2000 é bissexto
        self.assertEqual(lt.carencia(), 18)
        self.assertEqual(unir_periodos([(p.inicio, p.fim) for p in ps]),
                         [(D(2000, 1, 1), D(2001, 6, 30))])

    def test_periodos_contiguos_se_unem(self):
        self.assertEqual(unir_periodos([(D(2000, 1, 1), D(2000, 1, 31)), (D(2000, 2, 1), D(2000, 2, 29))]),
                         [(D(2000, 1, 1), D(2000, 2, 29))])

    def test_periodo_contido_em_outro(self):
        ps = [Periodo(D(2010, 1, 1), D(2010, 12, 31)), Periodo(D(2010, 3, 1), D(2010, 3, 31))]
        self.assertEqual(LinhaDoTempo(ps, "F").tempo_bruto(), 365)

    def test_fatores_decreto_3048_art70(self):
        self.assertEqual(fator_conversao("especial25", "M"), 1.40)
        self.assertEqual(fator_conversao("especial20", "M"), 1.75)
        self.assertEqual(fator_conversao("especial15", "M"), 2.33)
        self.assertEqual(fator_conversao("especial25", "F"), 1.20)
        self.assertEqual(fator_conversao("especial20", "F"), 1.50)
        self.assertEqual(fator_conversao("especial15", "F"), 2.00)
        self.assertEqual(fator_conversao("comum", "M"), 1.0)
        self.assertEqual(fator_conversao("professor", "F"), 1.0)

    def test_conversao_so_ate_13_11_2019(self):
        # 04/11 a 23/11/2019: 10 dias até 13/11 (convertidos) + 10 depois (não)
        lt = LinhaDoTempo([Periodo(D(2019, 11, 4), D(2019, 11, 23), "especial25")], "M")
        self.assertEqual(lt.tempo_bruto(), 20)
        self.assertAlmostEqual(lt.tempo_contribuicao(), 10 * 1.4 + 10)
        self.assertAlmostEqual(lt.acrescimo_conversao(), 4.0)
        self.assertAlmostEqual(lt.tempo_contribuicao(DATA_EC103), 14.0)

    def test_dia_13_11_2019_ainda_converte(self):
        lt = LinhaDoTempo([Periodo(D(2019, 11, 13), D(2019, 11, 13), "especial15")], "F")
        self.assertAlmostEqual(lt.tempo_contribuicao(), 2.0)

    def test_especial_depois_da_ec_nao_converte(self):
        lt = LinhaDoTempo([Periodo(D(2020, 1, 1), D(2020, 12, 31), "especial25")], "M")
        self.assertAlmostEqual(lt.tempo_contribuicao(), 366)
        self.assertAlmostEqual(lt.acrescimo_conversao(), 0)

    def test_conversao_mulher_especial15(self):
        lt = LinhaDoTempo([Periodo(D(2010, 1, 1), D(2010, 1, 10), "especial15")], "F")
        self.assertAlmostEqual(lt.tempo_contribuicao(), 20.0)

    def test_concomitancia_especial_e_comum_vale_maior_fator(self):
        ps = [Periodo(D(2019, 1, 1), D(2019, 1, 10), "especial25"), Periodo(D(2019, 1, 1), D(2019, 1, 10), "comum")]
        lt = LinhaDoTempo(ps, "M")
        self.assertEqual(lt.tempo_bruto(), 10)
        self.assertAlmostEqual(lt.tempo_contribuicao(), 14.0)  # não 24

    def test_carencia_mes_parcial_conta_inteiro(self):
        lt = LinhaDoTempo([Periodo(D(2020, 1, 15), D(2020, 3, 10))], "M")
        self.assertEqual(lt.carencia(), 3)

    def test_carencia_concomitante_no_mesmo_mes_conta_uma_vez(self):
        ps = [Periodo(D(2020, 1, 1), D(2020, 1, 10)), Periodo(D(2020, 1, 20), D(2020, 1, 31))]
        self.assertEqual(LinhaDoTempo(ps, "M").carencia(), 1)

    def test_competencia_sem_contribuicao_nao_conta(self):
        p = Periodo(D(2020, 1, 1), D(2020, 12, 31), "comum", competencias_sem_contribuicao=["2020-05"])
        lt = LinhaDoTempo([p], "F")
        self.assertEqual(lt.carencia(), 11)
        self.assertEqual(lt.tempo_bruto(), 366 - 31)

    def test_acrescimo_da_conversao_nao_conta_carencia(self):
        lt = LinhaDoTempo([Periodo(D(2000, 1, 1), D(2000, 12, 31), "especial25")], "M")
        self.assertEqual(lt.carencia(), 12)

    def test_carencia_ate_data(self):
        lt = LinhaDoTempo([Periodo(D(2020, 1, 1), D(2020, 12, 31))], "M")
        self.assertEqual(lt.carencia(D(2020, 6, 1)), 6)
        self.assertEqual(lt.carencia(D(2019, 12, 31)), 0)

    def test_rural(self):
        lt = LinhaDoTempo([Periodo(D(1985, 1, 1), D(1985, 12, 31), "rural")], "M")
        self.assertEqual(lt.tempo_bruto(), 365)
        self.assertEqual(lt.carencia(), 0)
        lt2 = LinhaDoTempo([Periodo(D(1995, 1, 1), D(1995, 12, 31), "rural")], "M")
        self.assertEqual(lt2.tempo_bruto(), 0)
        lt3 = LinhaDoTempo([Periodo(D(1995, 1, 1), D(1995, 12, 31), "rural", com_contribuicao=True)], "M")
        self.assertEqual((lt3.tempo_bruto(), lt3.carencia()), (365, 12))

    def test_magisterio(self):
        ps = [Periodo(D(2000, 1, 1), D(2000, 12, 31), "professor"), Periodo(D(2001, 1, 1), D(2001, 1, 31))]
        lt = LinhaDoTempo(ps, "F")
        self.assertEqual(lt.tempo_magisterio(), 366)
        self.assertEqual(lt.tempo_bruto(), 397)

    def test_convencao_365_30(self):
        self.assertEqual(dias_para_amd(12775), (35, 0, 0))
        self.assertEqual(dias_para_amd(400), (1, 1, 5))
        self.assertEqual(dias_para_amd(14.9), (0, 0, 14))  # trunca

    def test_resumo_calcular_tempo(self):
        r = calcular_tempo([Periodo(D(2019, 11, 4), D(2019, 11, 23), "especial25")], "M")
        self.assertEqual(r["tempo_bruto_dias"], 20)
        self.assertAlmostEqual(r["tempo_ate_ec103_dias"], 14.0)
        self.assertAlmostEqual(r["periodos"][0]["dias_convertidos"], 24.0)

    def test_periodo_invalido(self):
        with self.assertRaises(ValueError):
            Periodo(D(2020, 2, 1), D(2020, 1, 1))
        with self.assertRaises(ValueError):
            Periodo(D(2020, 1, 1), D(2020, 2, 1), "especial30")


# ===========================================================================
# periodo_graca.py
# ===========================================================================
class TestPeriodoGraca(unittest.TestCase):
    def test_bug_31_12_2024(self):
        """Caso real do bug: 31/12/2024 + 12 meses deve perder em 16/02/2026, não em março."""
        r = calcular_periodo_graca(D(2024, 12, 31))
        self.assertEqual(r["mantem_ate"], D(2026, 2, 15))
        self.assertEqual(r["perde_em"], D(2026, 2, 16))
        self.assertEqual(r["fim_prazo_competencia"], (2025, 12))

    def test_dias_29_30_31_dao_o_mesmo_resultado(self):
        for dia in (1, 15, 29, 30, 31):
            self.assertEqual(calcular_periodo_graca(D(2024, 12, dia))["perde_em"], D(2026, 2, 16))
        self.assertEqual(calcular_periodo_graca(D(2024, 1, 31))["perde_em"], D(2025, 3, 16))
        self.assertEqual(calcular_periodo_graca(D(2024, 2, 29))["perde_em"], D(2025, 4, 16))

    def test_somar_meses_competencia(self):
        self.assertEqual(somar_meses(2024, 12, 14), (2026, 2))
        self.assertEqual(somar_meses(2024, 11, 2), (2025, 1))
        self.assertEqual(somar_meses(2024, 1, 0), (2024, 1))

    def test_prorrogacoes(self):
        self.assertEqual(calcular_periodo_graca(D(2024, 12, 31), mais_de_120=True)["perde_em"], D(2027, 2, 16))
        self.assertEqual(calcular_periodo_graca(D(2024, 12, 31), desemprego=True)["perde_em"], D(2027, 2, 16))
        r = calcular_periodo_graca(D(2024, 12, 31), mais_de_120=True, desemprego=True)
        self.assertEqual((r["meses_graca"], r["perde_em"]), (36, D(2028, 2, 16)))

    def test_facultativo_6_meses_sem_prorrogacao(self):
        r = calcular_periodo_graca(D(2024, 12, 31), "facultativo", mais_de_120=True, desemprego=True)
        self.assertEqual((r["meses_graca"], r["perde_em"]), (6, D(2025, 8, 16)))

    def test_data_perda(self):
        self.assertEqual(data_perda_qualidade((2024, 12), 12), D(2026, 2, 16))

    def test_qualidade_na_data(self):
        iv = [(D(2000, 1, 1), D(2005, 12, 31))]
        self.assertTrue(analisar_qualidade(iv, D(2007, 2, 15))["segurado"])
        self.assertFalse(analisar_qualidade(iv, D(2007, 2, 16))["segurado"])
        self.assertEqual(analisar_qualidade(iv, D(2005, 6, 1))["situacao"], "contribuindo na data de referência")

    def test_mais_de_120_literal(self):
        com_121 = [(D(2000, 1, 1), D(2010, 1, 31))]   # 121 competências
        com_120 = [(D(2000, 1, 1), D(2009, 12, 31))]  # 120 competências
        self.assertEqual(analisar_qualidade(com_121, D(2011, 1, 1))["meses_graca"], 24)
        self.assertEqual(analisar_qualidade(com_120, D(2011, 1, 1))["meses_graca"], 12)
        self.assertEqual(analisar_qualidade(com_120, D(2011, 1, 1), minimo_120_inclusive=True)["meses_graca"], 24)

    def test_historico_com_perda(self):
        iv = [(D(2000, 1, 1), D(2000, 12, 31)), (D(2002, 3, 1), D(2002, 12, 31))]
        r = analisar_qualidade(iv, D(2003, 1, 10))
        self.assertEqual(len(r["perdas"]), 1)
        self.assertEqual(r["perdas"][0]["perdeu_em"], D(2002, 2, 16))
        self.assertEqual(r["contribuicoes_sequencia"], 10)

    def test_historico_volta_antes_da_perda(self):
        iv = [(D(2000, 1, 1), D(2000, 12, 31)), (D(2002, 2, 10), D(2002, 12, 31))]
        r = analisar_qualidade(iv, D(2003, 1, 10))
        self.assertEqual(r["perdas"], [])
        self.assertEqual(r["contribuicoes_sequencia"], 23)

    def test_prorrogacao_120_apos_perda_conforme_criterio(self):
        # 121 contribuições, perda, depois 12 meses e nova saída
        iv = [(D(1990, 1, 1), D(2000, 1, 31)), (D(2005, 1, 1), D(2005, 12, 31))]
        a = analisar_qualidade(iv, D(2006, 6, 1), criterio_120="qualquer_sequencia")
        b = analisar_qualidade(iv, D(2006, 6, 1), criterio_120="sequencia_atual")
        self.assertEqual(len(a["perdas"]), 1)
        self.assertEqual(a["meses_graca"], 24)
        self.assertEqual(b["meses_graca"], 12)


# ===========================================================================
# regras_ec103.py - tabelas
# ===========================================================================
class TestTabelas(unittest.TestCase):
    def test_art15_pontos_ano_a_ano(self):
        mulher = {a: pontos_art15("F", a) for a in range(2019, 2035)}
        self.assertEqual(mulher[2019], 86)
        self.assertEqual(mulher[2025], 92)
        self.assertEqual(mulher[2032], 99)
        self.assertEqual(mulher[2033], 100)
        self.assertEqual(mulher[2034], 100)
        homem = {a: pontos_art15("M", a) for a in range(2019, 2031)}
        self.assertEqual([homem[a] for a in range(2019, 2030)], [96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 105])
        self.assertEqual([pontos_art15("F", a, True) for a in (2019, 2029, 2030, 2031)], [81, 91, 92, 92])
        self.assertEqual([pontos_art15("M", a, True) for a in (2019, 2027, 2028, 2029)], [91, 99, 100, 100])

    def test_art16_idade_ano_a_ano(self):
        mulher = [idade_art16_meses("F", a) / 12 for a in range(2019, 2033)]
        self.assertEqual(mulher, [56, 56.5, 57, 57.5, 58, 58.5, 59, 59.5, 60, 60.5, 61, 61.5, 62, 62])
        homem = [idade_art16_meses("M", a) / 12 for a in range(2019, 2029)]
        self.assertEqual(homem, [61, 61.5, 62, 62.5, 63, 63.5, 64, 64.5, 65, 65])
        self.assertEqual(idade_art16_meses("F", 2025), 59 * 12)        # 2025: 59 anos (não 59a6m)
        self.assertEqual(idade_art16_meses("F", 2026), 59 * 12 + 6)    # 59a6m é a exigência de 2026
        self.assertEqual([idade_art16_meses("F", a, True) / 12 for a in (2019, 2030, 2031, 2032)], [51, 56.5, 57, 57])
        self.assertEqual([idade_art16_meses("M", a, True) / 12 for a in (2019, 2026, 2027, 2028)], [56, 59.5, 60, 60])

    def test_art18_idade_mulher(self):
        self.assertEqual([idade_art18_meses("F", a) / 12 for a in range(2019, 2025)], [60, 60.5, 61, 61.5, 62, 62])
        self.assertEqual(idade_art18_meses("M", 2030), 65 * 12)

    def test_coeficiente_art26(self):
        self.assertEqual(coeficiente_art26(15 * 365, "F"), 0.60)
        self.assertEqual(coeficiente_art26(20 * 365, "F"), 0.70)
        self.assertEqual(coeficiente_art26(20 * 365, "M"), 0.60)
        self.assertEqual(coeficiente_art26(25 * 365 - 1, "M"), 0.68)  # 24a completos
        self.assertEqual(coeficiente_art26(40 * 365, "M"), 1.00)
        self.assertEqual(coeficiente_art26(40 * 365, "F"), 1.10)      # não limitado a 100% [CONFERIR]

    def test_idade_e_meses(self):
        self.assertEqual(idade_amd(D(1966, 1, 10), D(2025, 7, 10)), (59, 6, 0))
        self.assertEqual(idade_amd(D(1966, 1, 10), D(2025, 7, 9)), (59, 5, 29))
        self.assertEqual(somar_meses_data(D(2020, 2, 29), 12), D(2021, 3, 1))
        self.assertEqual(somar_meses_data(D(2000, 1, 31), 1), D(2000, 3, 1))


# ===========================================================================
# regras_ec103.py - simulação em datas-limite
# ===========================================================================
LONGO = Periodo(D(1985, 1, 1), D(2040, 12, 31))  # tempo e carência de sobra


class TestRegras(unittest.TestCase):
    def test_art16_mulher_30_anos_e_59a6m_em_2025(self):
        """Completa 30 anos de contribuição em 10/07/2025, dia em que faz 59a6m.
        Em 2025 a exigência é 59 anos -> cumpre em 10/07/2025 (a véspera não)."""
        fim30 = D(2025, 7, 10)
        p = Periodo(fim30 - timedelta(days=30 * 365 - 1), D(2030, 12, 31))
        seg = Segurado(D(1966, 1, 10), "F")
        r = regra(simular_regras([p], seg, D(2025, 12, 31)), "ART16")
        self.assertEqual(r.data_cumprimento, D(2025, 7, 10))
        self.assertTrue(r.cumpre)
        lt = LinhaDoTempo([p], "F")
        self.assertLess(lt.tempo_contribuicao(D(2025, 7, 9)), 30 * 365)

    def test_art16_mulher_59_anos_em_dezembro_de_2025(self):
        r = regra(simular_regras([LONGO], Segurado(D(1966, 12, 20), "F"), D(2026, 1, 1)), "ART16")
        self.assertEqual(r.data_cumprimento, D(2025, 12, 20))

    def test_art16_mulher_que_faz_59_em_2026_precisa_59a6m(self):
        r = regra(simular_regras([LONGO], Segurado(D(1967, 1, 10), "F"), D(2026, 1, 1)), "ART16")
        self.assertEqual(r.data_cumprimento, D(2026, 7, 10))
        self.assertFalse(r.cumpre)
        self.assertTrue(any("idade" in f for f in r.faltantes))

    def test_art16_homem_64a6m_em_2026(self):
        r = regra(simular_regras([LONGO], Segurado(D(1962, 3, 1), "M"), D(2026, 1, 1)), "ART16")
        self.assertEqual(r.data_cumprimento, D(2026, 9, 1))

    def test_art15_homem_tempo_congelado(self):
        """35a exatos até 2018; nascido 15/06/1959: só alcança no teto de 105 (70 anos).
        [CONFERIR] No método "amd" (base 30/360) a idade de 14/06/2029 é 69a 11m 30d
        (maio tem 31 dias) e 30 dias normalizam para 1 mês -> 105 pontos um dia ANTES
        do aniversário. No método "decimal" a data é o próprio aniversário."""
        p = periodo_com_dias(D(2018, 12, 31), 35 * 365)
        seg = Segurado(D(1959, 6, 15), "M")
        r = regra(simular_regras([p], seg, D(2026, 1, 1)), "ART15")
        self.assertEqual(r.data_cumprimento, D(2029, 6, 14))
        self.assertEqual(r.coeficiente, 0.90)  # 60% + 2% x (35-20)
        r_dec = regra(simular_regras([p], seg, D(2026, 1, 1), opcoes=Opcoes(metodo_pontos="decimal")), "ART15")
        self.assertEqual(r_dec.data_cumprimento, D(2029, 6, 15))
        # em 2028 (exigência já no teto de 105) ainda não alcança
        self.assertGreater(r.data_cumprimento, D(2028, 12, 31))

    def test_art15_mulher_teto_100_em_2033(self):
        p = periodo_com_dias(D(2018, 12, 31), 30 * 365)
        r = regra(simular_regras([p], Segurado(D(1975, 3, 10), "F"), D(2026, 1, 1)), "ART15")
        self.assertEqual(r.data_cumprimento, D(2045, 3, 10))

    def test_art15_data_encontrada_e_a_primeira(self):
        p = Periodo(D(1995, 1, 1), D(2035, 12, 31))
        seg = Segurado(D(1965, 1, 1), "F")
        r = regra(simular_regras([p], seg, D(2025, 1, 1)), "ART15")
        from regras_ec103 import _Contexto
        ctx = _Contexto(LinhaDoTempo([p], "F"), seg, Opcoes())
        d = r.data_cumprimento
        self.assertTrue(ctx.pontos_ok(d, pontos_art15("F", d.year), "tc"))
        self.assertFalse(ctx.pontos_ok(d - timedelta(days=1), pontos_art15("F", (d - timedelta(days=1)).year), "tc"))

    def test_art17_bloqueado_homem_com_33_exatos(self):
        p = periodo_com_dias(DATA_EC103, 33 * 365)
        r = regra(simular_regras([p], Segurado(D(1970, 1, 1), "M"), D(2026, 1, 1), projetar=True), "ART17")
        self.assertFalse(r.aplicavel)
        self.assertIn("MAIS DE 33", r.motivo_inaplicavel)

    def test_art17_bloqueado_mulher_com_27_anos(self):
        p = periodo_com_dias(DATA_EC103, 27 * 365)
        r = regra(simular_regras([p], Segurado(D(1970, 1, 1), "F"), D(2026, 1, 1), projetar=True), "ART17")
        self.assertFalse(r.aplicavel)

    def test_art17_liberado_e_pedagio_50(self):
        dias2019 = 33 * 365 + 1
        inicio = DATA_EC103 - timedelta(days=dias2019 - 1)
        p = Periodo(inicio, D(2030, 12, 31))
        r = regra(simular_regras([p], Segurado(D(1970, 1, 1), "M"), D(2026, 1, 1)), "ART17")
        self.assertTrue(r.aplicavel)
        exigido = 35 * 365 + 0.5 * (35 * 365 - dias2019)  # 13.139,5 dias
        self.assertEqual(r.data_cumprimento, inicio + timedelta(days=13140 - 1))
        self.assertTrue(r.com_fator)
        self.assertAlmostEqual(exigido, 13139.5)

    def test_art20_pedagio_100(self):
        inicio = DATA_EC103 - timedelta(days=30 * 365 - 1)  # 30 anos em 13/11/2019
        p = Periodo(inicio, D(2035, 12, 31))
        r = regra(simular_regras([p], Segurado(D(1960, 1, 1), "M"), D(2026, 1, 1)), "ART20")
        self.assertEqual(r.data_cumprimento, inicio + timedelta(days=40 * 365 - 1))  # 35 + 5
        self.assertEqual(r.coeficiente, 1.0)

    def test_art20_mulher_idade_57(self):
        r = regra(simular_regras([LONGO], Segurado(D(1966, 5, 5), "F"), D(2026, 1, 1)), "ART20")
        self.assertEqual(r.data_cumprimento, D(2023, 5, 5))

    def test_art18_mulher(self):
        r = regra(simular_regras([LONGO], Segurado(D(1962, 5, 5), "F"), D(2026, 1, 1)), "ART18")
        self.assertEqual(r.data_cumprimento, D(2024, 5, 5))  # 2023 exige 62; fez 61
        r = regra(simular_regras([LONGO], Segurado(D(1960, 1, 10), "F"), D(2026, 1, 1)), "ART18")
        self.assertEqual(r.data_cumprimento, D(2020, 7, 10))  # 2020 exige 60a6m

    def test_art19_homem_filiado_depois_exige_20_anos(self):
        inicio = D(2020, 1, 1)
        p = Periodo(inicio, D(2050, 12, 31))
        res = simular_regras([p], Segurado(D(1965, 1, 1), "M"), D(2026, 1, 1))
        r = regra(res, "ART19")
        self.assertEqual(r.data_cumprimento, inicio + timedelta(days=20 * 365 - 1))
        self.assertEqual(r.coeficiente, 0.60)
        self.assertFalse(regra(res, "ART16").aplicavel)
        self.assertFalse(regra(res, "ART20").aplicavel)

    def test_art19_homem_filiado_antes_exige_15(self):
        p = periodo_com_dias(D(2019, 1, 31), 15 * 365)
        r = regra(simular_regras([p], Segurado(D(1960, 6, 1), "M"), D(2026, 1, 1)), "ART19")
        self.assertEqual(r.data_cumprimento, D(2025, 6, 1))

    def test_direito_adquirido(self):
        p = periodo_com_dias(D(2019, 6, 30), 35 * 365)
        res = simular_regras([p], Segurado(D(1960, 6, 1), "M"), D(2026, 1, 1))
        da = regra(res, "DA-TC")
        self.assertEqual(da.data_cumprimento, D(2019, 6, 30))
        self.assertTrue(da.com_fator)
        # 35a + idade 59a0m29d em 30/06/2019 = 94 < 96 -> não cumpre pontos até 13/11/2019
        self.assertIsNone(regra(res, "DA-PT").data_cumprimento)

    def test_direito_adquirido_pontos_95_antes_de_31_12_2018(self):
        p = periodo_com_dias(D(2018, 6, 30), 35 * 365)
        r = regra(simular_regras([p], Segurado(D(1958, 6, 30), "M"), D(2026, 1, 1)), "DA-PT")
        self.assertEqual(r.data_cumprimento, D(2018, 6, 30))  # 60 + 35 = 95 em 2018

    def test_sem_projecao_nao_inventa_tempo(self):
        p = periodo_com_dias(D(2020, 12, 31), 20 * 365)
        r = regra(simular_regras([p], Segurado(D(1970, 1, 1), "F"), D(2026, 1, 1)), "ART16")
        self.assertIsNone(r.data_cumprimento)
        self.assertTrue(any("tempo de contribuição" in f for f in r.faltantes))

    def test_conversao_especial_entra_no_tempo_das_regras(self):
        # 25 anos especiais de homem até 13/11/2019 = 35 anos convertidos
        p = periodo_com_dias(DATA_EC103, 25 * 365, "especial25")
        res = simular_regras([p], Segurado(D(1970, 1, 1), "M"), D(2026, 1, 1))
        self.assertEqual(regra(res, "DA-TC").data_cumprimento, DATA_EC103)

    def test_professora(self):
        p = Periodo(D(1995, 1, 1), D(2040, 12, 31), "professor")
        res = simular_regras([p], Segurado(D(1972, 3, 1), "F"), D(2026, 1, 1))
        r = regra(res, "ART16-P")
        # tempo 25 anos em 2019; idade exigida em 2025 = 54 -> faz 54 em 01/03/2026 (2026 exige 54a6m)
        self.assertEqual(r.data_cumprimento, D(2026, 9, 1))


class TestSimular(unittest.TestCase):
    def test_relatorio_exemplo(self):
        import simular
        aqui = os.path.dirname(os.path.abspath(__file__))
        caso = simular.carregar_caso(os.path.join(aqui, "exemplo_caso.json"))
        txt = simular.gerar_relatorio(caso)
        self.assertIn("Simulação de apoio. Não substitui o cálculo no software do escritório nem a conferência da advogada.", txt)
        for trecho in ("Quadro de períodos", "Carência", "Qualidade de segurado", "Regras de aposentadoria",
                       "Melhor regra", "[CONFERIR]"):
            self.assertIn(trecho, txt)


if __name__ == "__main__":
    unittest.main()
