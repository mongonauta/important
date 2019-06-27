import sys
import types

from flask import Flask
from flask import request
from types import ModuleType

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


method_code = """
def hello():
    return 'Hello, World'
"""

method_code2 = """
def hello():
    return 'Hello, World 2'
"""


def get_end_point(code):
    tmp_module = ModuleType('tmp_module')
    exec(code, tmp_module.__dict__)
    sys.modules['tmp_module'] = tmp_module

    return [
        (key, value)
        for key, value in tmp_module.__dict__.items()
        if isinstance(value, types.FunctionType)
    ][0]


@app.route('/loader')
def loader():
    new_end_point = get_end_point(method_code)
    app.route(f'/{new_end_point[0]}')(new_end_point[1])

    return 'ok'


@app.route('/updater')
def updater():
    new_end_point = get_end_point(method_code2)
    app.view_functions[new_end_point[0]] = new_end_point[1]

    return 'ok'


@app.route('/post_loader', methods=['post'])
def post_loader():
    new_end_point = get_end_point(request.data)
    app.view_functions[new_end_point[0]] = new_end_point[1]

    return 'ok'


if __name__ == "__main__":
    print('http://127.0.0.1:5000/hello')
    print('http://127.0.0.1:5000/loader')
    print('http://127.0.0.1:5000/updater')

    app.run()
