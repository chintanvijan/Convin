from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
import requests
from datetime import datetime,date

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'convin.settings')
app = Celery('convin')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
   
    sender.add_periodic_task(10.0, debug_task, name='add every 10')

   
    sender.add_periodic_task(30.0, debug_task, expires=10)

    
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        debug_task,
    )



@app.task(bind=True)
def debug_task(self):
    # print('Request: {0!r}'.format(self.request))
    today = datetime.today().weekday()
    now = datetime.now()
    day = now.strftime("%d")
    hour = now.strftime("%H")
    # print(today)
    r = requests.get('http://localhost:8000/task-tracker/')
    data = r.json()
    for i in data:
    	if str(today) == str(0):
    		if i['update_type'] == 2 and i['status']=='Pending':
    			print('Weekly :',i['email'])
    			requests.post('http://localhost:8000/task-tracker/'+str(i['id']))
    	if str(day) == str(1) and i['status']=='Pending':
    		if i['update_type'] == 1:
    			print('Monthly :',i['email'])
    			requests.post('http://localhost:8000/task-tracker/'+str(i['id']))
    	if str(hour) == str(17) and i['status']=='Pending':
    		if i['update_type'] == 3:
    			print('Daily :',i['email'])
    			requests.post('http://localhost:8000/task-tracker/'+str(i['id']))