from rest_framework import generics
from rest_framework.response import Response
from core.serializers import TaskSerializer, ProjectSerializer
from core.models import Task, Project


class ProjectListCreateView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TaskListCreateView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

