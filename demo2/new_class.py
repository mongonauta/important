import importlib.util
import sys

source_code = """
class Hello:
    _str = None
    
    def __init__(self, name):
        self._str = f'Hola chatos. Soy {name}'
    
    def run(self):
        return self._str

"""

if __name__ == '__main__':
    spec = importlib.util.find_spec('demo2.new_class')
    current_module = importlib.util.module_from_spec(spec)

    code_obj = compile(source_code, current_module.__spec__.origin, 'exec')

    exec(code_obj, current_module.__dict__)

    sys.modules['demo2.new_class'] = current_module

    obj1 = current_module.Hello('objeto 1')
    obj2 = current_module.Hello('objeto 2')
    print(obj1.run())
    print(obj2.run())
