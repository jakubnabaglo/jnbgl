import flask

app = flask.Flask(__name__)


@app.before_request
def force_ssl():
    if flask.request.headers['X-Forwarded-Proto'] != 'https':
        return flask.redirect('https://{}{}'.format(
            flask.request.headers['host'],
            flask.request.path))


@app.route('/')
def home():
    return 'Hello there.'


if __name__ == '__main__':
    import os
    app.run(port=int(os.environ['PORT']), debug=True, host='0.0.0.0')
