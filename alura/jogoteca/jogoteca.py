from flask import Flask, render_template, request

app = Flask(__name__)


class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


tetris = Jogo('Tetris',  'ação', 'Nintendo')
mario = Jogo('Mario',  'ação', 'Nintendo')
pokemon = Jogo('Pokemon',  'aventura', 'Nintendo')
jogos = [tetris, mario, pokemon]


@app.route('/')
def index():
    return render_template('lista_jogos.html', titulo='Jogos', jogos=jogos)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    novo_jogo = Jogo(nome, categoria, console)
    jogos.append(novo_jogo)
    return render_template('lista_jogos.html', titulo='Jogos', jogos=jogos)


# app.run(host='0.0.0.0', port=8080)
app.run(debug=True)

