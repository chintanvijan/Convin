from django.contrib import admin
from .models import Task,update_types,TaskTracker
# Register your models here.
admin.site.register(Task)
admin.site.register(update_types)
admin.site.register(TaskTracker)
