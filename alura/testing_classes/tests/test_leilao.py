from unittest import TestCase

from alura.projeto_testes.src.leilao.dominio import Usuario, Lance, Leilao
from alura.projeto_testes.src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('GUI', 500.0)
        self.lance_gui = Lance(self.gui, 100.0)
        self.leilao = Leilao('Celular')

    def test_retornar_o_maior_e_menor_valor_de_lance_crescente(self):
        self.leilao.propoe(self.lance_gui)

        yuri = Usuario('Yuri', 500.0)
        lance_yuri = Lance(yuri, 150.0)
        self.leilao.propoe(lance_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_retornar_o_maior_e_menor_valor_de_lance_decrescente(self):
        self.leilao.propoe(self.lance_gui)

        yuri = Usuario('Yuri', 500.0)
        lance_yuri = Lance(yuri, 150.0)
        self.leilao.propoe(lance_yuri)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_lance_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_gui)

            vini = Usuario('Vini', 500.0)
            lance_vini = Lance(vini, 200.0)
            self.leilao.propoe(lance_vini)

            yuri = Usuario('Yuri', 500.0)
            lance_yuri = Lance(yuri, 150.0)
            self.leilao.propoe(lance_yuri)

    def test_retornar_maioremenor_comtres_lances(self):
        self.leilao.propoe(self.lance_gui)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 100.0
        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    # se nao tem lance, permite propor lance
    def test_deve_permitir_propor_lance(self):
        self.leilao.propoe(self.lance_gui)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(1, quantidade_lances_recebido)

    # se o ultimo user for diferente, permitte propor lance
    def test_propor_lance_ultimo_user_diferente(self):
        yuri = Usuario('Yuri', 500.0)
        lance_yuri = Lance(yuri, 200.0)
        self.leilao.propoe(self.lance_gui)
        self.leilao.propoe(lance_yuri)

        quantidade_lances_recebido = len(self.leilao.lances)
        self.assertEqual(2, quantidade_lances_recebido)

    # se ultimo usuaio for o mesmo, nao deve permitir propor lance
    def test_nao_podepropor_lance_ultimo_user_igual(self):
        lance_gui_2 = Lance(self.gui, 200.0)

        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_gui)
            self.leilao.propoe(lance_gui_2)


