import random

import flask

app = flask.Flask(__name__)


@app.route('/')
def home():
    return flask.render_template('home.html')


@app.route('/projects/')
def projects():
    ken = random.choices([False, True], cum_weights=[.8, 1])[0]
    return flask.render_template('projects.html', ken=ken)


@app.route('/projects/redshift/')
def photometric_redshift():
    return flask.render_template('redshift.html')


@app.route('/projects/voting/')
def homomorphic_counting():
    return flask.render_template('voting.html')


@app.route('/hutter/')
def hutter():
    return flask.render_template('hutter.html')


if __name__ == '__main__':
    import os
    app.run(port=int(os.environ['PORT']), debug=True, host='0.0.0.0')
