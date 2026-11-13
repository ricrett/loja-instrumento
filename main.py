from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def inicial ():
    return render_template ('usuarios/index.html')

@app.route('/index', methods=['GET', 'POST'])
def index ():
    return render_template ('usuarios/index.html')

@app.route('/cadastros', methods=['GET', 'POST'])
def cadastros ():
    return render_template ('usuarios/cadastros.html')

@app.route('/listagem', methods=['GET', 'POST'])
def listagem ():
    return render_template ('usuarios/listagem.html')

if __name__ == '__main__':
    app.run(debug=True)