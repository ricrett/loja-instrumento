import os

from dotenv import load_dotenv
from flask import Flask, redirect, render_template, url_for
from flask_wtf.csrf import CSRFProtect

from db import execute_one

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
CSRFProtect(app)

@app.route('/', methods=['GET', 'POST'])
def inicial ():
    return render_template ('usuarios/dashboard.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard ():
    perfis = execute_one('SELECT COUNT(*) AS total FROM perfis')
    usuarios = execute_one('SELECT COUNT(*) AS total FROM usuarios')
    produtos = execute_one('SELECT COUNT(*) AS total FROM produtos')

    return render_template('dashboard.html', titulo='Sistema de Gestão',
                           total_perfis=perfis['total'],
                           total_usuarios=usuarios['total'],
                           total_produtos=produtos['total'])

@app.route('/cadastros', methods=['GET', 'POST'])
def cadastros ():
    return render_template ('usuarios/cadastros.html')

@app.route('/listagem', methods=['GET', 'POST'])
def listagem ():
    return render_template ('usuarios/listagem.html')

@app.errorhandler(404)
def pagina_nao_encontrada(erro):
    return render_template('404.html'), 404


@app.errorhandler(500)
def erro_no_servidor(erro):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)