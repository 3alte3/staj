from __future__ import absolute_import,unicode_literals

from celery import shared_task

@shared_task(bind=True)
def do(x,y):
    return x+y