import os
from urllib.parse import unquote, urlsplit

import pymysql
from dotenv import load_dotenv
from flask import Flask, abort, redirect, render_template, request, url_for

load_dotenv()

app = Flask(__name__)

database_url = os.getenv('DATABASE_URL')
if not database_url:
    raise RuntimeError('A variável de ambiente DATABASE_URL não foi definida.')

database = urlsplit(database_url)
if database.scheme not in {'mysql', 'mysql+pymysql'} or not database.hostname:
    raise RuntimeError('DATABASE_URL deve usar o formato mysql:// ou mysql+pymysql://.')

database_name = unquote(database.path.lstrip('/'))
if not database_name:
    raise RuntimeError('DATABASE_URL deve informar o nome do banco de dados.')

database_config = {
    'host': database.hostname,
    'port': database.port or 3306,
    'user': unquote(database.username or ''),
    'password': unquote(database.password or ''),
    'database': database_name,
    'charset': 'utf8mb4',
}


def get_db_connection():
    return pymysql.connect(**database_config)


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

    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                'INSERT INTO resposta (nome, email, modelo, motivo) '
                'VALUES (%(nome)s, %(email)s, %(modelo)s, %(motivo)s)',
                fields,
            )
        connection.commit()
    return redirect(url_for('index'))


@app.route('/listar', methods=['GET'])
def listar():
    with get_db_connection() as connection:
        with connection.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(
                'SELECT id, nome, email, modelo, motivo '
                'FROM resposta ORDER BY id'
            )
            respostas = cursor.fetchall()
    return render_template('listar.html', respostas=respostas)


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