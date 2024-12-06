from rest_framework import viewsets
from .models import Client, Project, Task, Team
from django.contrib.auth.models import User
from .serializers import ClientSerializer, ProjectSerializer, TaskSerializer, TeamSerializer, UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_id') 
        status = self.request.query_params.get('status')
        if project_id:
            return Task.objects.filter(project_id=project_id)
        elif status:
            print(status)
            return Task.objects.filter(status=status)
        return Task.objects.all()
