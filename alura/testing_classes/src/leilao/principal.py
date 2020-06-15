from alura.projeto_testes.src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

gui = Usuario('GUI')
yuri = Usuario('Yuri')


lance_gui = Lance(gui, 100.0)
lance_yui = Lance(yuri, 150.0)

leilao = Leilao('Celular')

leilao.lances.append(lance_gui)
leilao.lances.append(lance_yui)

[print(f"Lance {lance.usuario.nome} valor {lance.valor}")for lance in leilao.lances]


avaliador = Avaliador()
avaliador.avalia(leilao)

print(avaliador.menor_lance)
print(avaliador.maior_lance)