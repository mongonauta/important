import importlib.util
import sys

source_code = """
def hello_world():
    return "Hola chatos"

"""

if __name__ == '__main__':
    spec = importlib.util.find_spec('demo2.basic')
    current_module = importlib.util.module_from_spec(spec)

    code_obj = compile(source_code, current_module.__spec__.origin, 'exec')

    exec(code_obj, current_module.__dict__)

    sys.modules['demo2.basic'] = current_module

    print(current_module.hello_world())
