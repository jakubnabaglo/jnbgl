import flask

app = flask.Flask(__name__)

@app.before_request
def force_ssl():
    if flask.request.header['x-forwarded-proto'] != 'https':
        flask.redirect('https://{}{}'.format(
            flask.request.header['host'],
            flask.request.path))


@app.route('/')
def home():
    raise Exception()
    return 'Hello there.'


if __name__ == '__main__':
    import os
    app.run(port=os.environ['PORT'], debug=True, host='0.0.0.0')
