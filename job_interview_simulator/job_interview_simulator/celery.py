# job_interview_simulator/celery.py
from __future__ import absolute_import
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'job_interview_simulator.settings')

# Create a Celery instance and load settings
app = Celery('job_interview_simulator')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()