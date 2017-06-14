import flask

app = flask.Flask(__name__)


@app.before_request
def before_request():
    if flask.request.url.startswith('http://'):
        url = 'https://' + flask.request.url[7:]
        return flask.redirect(url, code=301)


@app.route('/')
def home():
    return 'Hello there.'


if __name__ == '__main__':
    app.run(debug=True)
