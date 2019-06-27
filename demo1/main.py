"""
https://www.tutorialspoint.com/the-implementation-of-import-in-python-importlib
https://docs.python.org/3/tutorial/modules.html

Load a function in execution time
"""
import importlib.util
import os

source_code = """
def hello_world():
    return "Hola chatos"

"""


def check_module(mod):
    spec = importlib.util.find_spec(mod)
    if spec is None:
        return None
    else:
        return spec


def import_module(spec):
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


if __name__ == '__main__':
    with open('new_func.py', 'w') as f:
        f.write(source_code)
        f.close()

        mod_spec = check_module('new_func')

        if mod_spec:
            new_mod = import_module(mod_spec)
            print(new_mod.hello_world())

        os.remove('new_func.py')
