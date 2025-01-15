from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ashker_credit_solution.settings')
app = Celery('ashker_credit_solution')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

----

# EXAMPLE: task to send reminders for due loans

from celery import shared_task

@shared_task
def send_due_reminder(user_id, loan_id):
    # Logic to send reminder to user
    pass

----
