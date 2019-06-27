from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


def hello():
    return 'Hello, World'


@app.route('/loader')
def loader():
    app.route(f'/{hello.__name__}')(hello)

    return 'ok'


if __name__ == "__main__":
    print('http://127.0.0.1:5000/hello')
    print('http://127.0.0.1:5000/loader')
    app.run()
