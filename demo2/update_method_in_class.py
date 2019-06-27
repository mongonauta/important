import importlib.util
import sys
import types

source_code = """
class Hello:
    _name = None
    
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name
    
    def run(self):
        return f'Hola chatos. Soy "{self._name}"'

"""

method_code = """
def new_run(self):
    return f'Hola chatos. Soy "{self._name}" vitaminado'
"""


if __name__ == '__main__':
    spec = importlib.util.find_spec('demo2.update_method_in_obj')
    current_module = importlib.util.module_from_spec(spec)

    code_obj = compile(source_code + method_code, current_module.__spec__.origin, 'exec')

    exec(code_obj, current_module.__dict__)

    sys.modules['demo2.update_method_in_obj'] = current_module

    obj1 = current_module.Hello('objeto 1')
    obj2 = current_module.Hello('objeto 2')

    print(obj1.run())
    print(obj2.run())

    setattr(current_module.Hello, 'run', current_module.new_run)

    print(obj1.run())
    print(obj2.run())

    obj3 = current_module.Hello('objeto 3')
    print(obj3.run())
