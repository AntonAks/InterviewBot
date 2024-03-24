from celery import Celery

app = Celery('InterviewBot_new', broker='amqp://guest:guest@localhost//')