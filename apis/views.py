from django.shortcuts import render
from .models import Task,TaskTracker,update_types
from .serializers import TaskSerializer,TaskTrackerSerializer
from rest_framework import routers, serializers, viewsets
# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
	queryset = Task.objects.all()
	serializer_class = TaskSerializer

class TaskTrackerViewSet(viewsets.ModelViewSet):
	queryset = TaskTracker.objects.all()
	serializer_class = TaskTrackerSerializer

def update_tracker(request,idi):
	if request.POST:
		info = TaskTracker.objects.get(id=idi)
		info.status = 'Completed'
		info.save()