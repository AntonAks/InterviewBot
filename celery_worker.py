from celery import Celery
from settings import settings
from time import sleep
import random

celery_app = Celery(__name__)
celery_app.conf.broker_url = settings.celery_broker_url
celery_app.conf.result_backend = settings.celery_result_url
celery_app.autodiscover_tasks()

# Create a dummy (test) task and
@celery_app.task(name='Test celery task', bind=True)
def dummy_task(self):
    for i in range(5):
        print(f"Background task is running. Second(s): {i}")
        delay = random.randint(1, 5) # Set random time execution for the dummy task from 1 to 5 seconds
        sleep(delay)

