from django.db import models

# Create your models here.

class Task(models.Model):
	task_type = models.IntegerField()
	task_desc = models.CharField(max_length=1000)
	def __str__(self):
		return self.task_desc


class update_types(models.Model):
	update_type = models.CharField(max_length=255)
	def __str__(self):
		return self.update_type

class TaskTracker(models.Model):
	task_type = models.ForeignKey(Task,on_delete=models.CASCADE)
	update_type = models.ForeignKey(update_types,on_delete=models.CASCADE)
	email = models.EmailField()
	status = models.CharField(max_length=255,default='Pending')
	def __str__(self):
		return self.email 

