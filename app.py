from flask import Flask, redirect, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('landing.html')


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