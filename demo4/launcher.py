import time

from celery import Celery

# print(Celery().send_task(
#     name="tasks.add",
#     args=(4, 4)
# ))

print(Celery().send_task(name="tasks.loader"))

time.sleep(3)

print(Celery().send_task(name="tasks.hello"))
