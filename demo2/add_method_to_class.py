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


def new_run(self):
    return f'Hola chatos. Soy "{self._name}" vitaminado'


if __name__ == '__main__':
    spec = importlib.util.find_spec('demo2.add_method_to_class')
    current_module = importlib.util.module_from_spec(spec)

    code_obj = compile(source_code, current_module.__spec__.origin, 'exec')

    exec(code_obj, current_module.__dict__)

    sys.modules['demo2.add_method_to_class'] = current_module

    obj1 = current_module.Hello('objeto 1')
    obj2 = current_module.Hello('objeto 2')

    try:
        print(obj1.new_run())
    except AttributeError as e:
        print(f'"{obj1.get_name()}" error: {str(e)}')

    try:
        print(obj2.new_run())
    except AttributeError as e:
        print(f'"{obj2.get_name()}" error: {str(e)}')

    setattr(current_module.Hello, 'new_run', new_run)

    print(obj1.new_run())
    print(obj2.new_run())

    obj3 = current_module.Hello('objeto 3')
    print(obj3.new_run())
