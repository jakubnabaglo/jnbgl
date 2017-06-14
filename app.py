import flask

app = flask.Flask(__name__)

if __name__ != '__main__':
    @app.before_request
    def before_request():
        if flask.request.header['x-forwarded-proto'] != 'https':
            flask.redirect('https://{}{}'.format(
                flask.request.header['host'],
                flask.request.path))


@app.route('/')
def home():
    raise Exception()
    return 'Hello there.'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
