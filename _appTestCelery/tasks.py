import time
from celery import shared_task


@shared_task
def hello_world():
    for i in range(100):
        print('Hello World!')
        time.sleep(2)
