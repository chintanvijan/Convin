from celery import shared_task
import requests
from datetime import datetime,date
@shared_task
def send_mails():
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
		# print(i)

