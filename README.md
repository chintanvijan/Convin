# Convin
Demo task

Make sure to install all the requirements mentioned in "requirements.txt" using pip.

In order to run celery task - 
Change CELERY_BROKER_URL in "settings.py" file.
Output is logged into log file and changes are updated into database after each mail is transacted in order to avoid duplicasy.

API Responses - 
For Tasks :
http://localhost:8000/task/

For Task-Tracker :
http://localhost:8000/task-tracker/

Note : Domain is variable .

Admin Panel (To view Models and relations, manage data)
http://localhost:8000/admin

Admin Dashboard credentials - 
Username : admin
Password : password
