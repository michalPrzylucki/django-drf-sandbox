from rest_framework import generics
from rest_framework.response import Response
from core.serializers import TaskSerializer, ProjectSerializer
from core.models import Task, Project


class ProjectView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

