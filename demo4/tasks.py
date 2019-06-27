import celery
import types
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')


@app.task
def add(x, y):
    return x + y


class AnotherTask(app.Task):
    name = 'tasks.hello'

    def run(self, x, y):
        return 'Hola'


def hello():
    return 'Hola'


@app.task
def loader():
    # new_task_class = types.new_class(
    #     name=f'{hello.__name__.capitalize()}Task',
    #     bases=(celery.Task,)
    # )
    #
    # new_task_class.name = f'tasks.{hello.__name__}'
    # setattr(new_task_class, hello.__name__, hello)
    #
    # app.tasks.register(new_task_class())
    # HelloTask.bind(app)
    # app.tasks.register(HelloTask())

    func = app.task(hello)
    func()
    app.autodiscover_tasks(['tasks.hello'], force=True)
