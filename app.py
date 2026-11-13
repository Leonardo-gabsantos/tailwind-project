import os

import pymysql
from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

pymysql.install_as_MySQLdb()

load_dotenv()

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError('A variável de ambiente DATABASE_URL não foi definida.')

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    fields = {
        'nome': request.form.get('nome', '').strip(),
        'email': request.form.get('email', '').strip(),
        'modelo': request.form.get('modelo', '').strip(),
        'motivo': request.form.get('motivo', '').strip(),
    }
    if not all(fields.values()):
        abort(400, description='Todos os campos são obrigatórios.')

    db.session.execute(
        text(
            'INSERT INTO resposta (nome, email, modelo, motivo) '
            'VALUES (:nome, :email, :modelo, :motivo)'
        ),
        fields,
    )
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/index')
def index_alias():
    return redirect(url_for('index'))


@app.route('/index.html')
def index_html():
    return redirect(url_for('index'))


@app.route('/engineering')
def engineering():
    return render_template('engineering.html')


@app.route('/engineering.html')
def engineering_html():
    return redirect(url_for('engineering'))


@app.route('/heritage')
def heritage():
    return render_template('heritage.html')


@app.route('/heritage.html')
def heritage_html():
    return redirect(url_for('heritage'))


@app.route('/models')
def models():
    return render_template('models.html')


@app.route('/models.html')
def models_html():
    return redirect(url_for('models'))


@app.route('/simulator')
def simulator():
    return render_template('simulator.html')


@app.route('/simulator.html')
def simulator_html():
    return redirect(url_for('simulator'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)