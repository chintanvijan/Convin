from .models import Task,update_types,TaskTracker
from rest_framework import serializers
class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ['task_type', 'task_desc']

class TaskTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = ['id','task_type', 'update_type','email']