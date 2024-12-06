from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Client, Team, Project, Task
from api.serializers import (
    UserSerializer,
    ClientSerializer,
    TeamSerializer,
    ProjectSerializer,
    TaskSerializer,
)


class UserSerializerTest(TestCase):
    def test_user_serializer(self):
        user = User.objects.create(
            username="testuser",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
        )
        serializer = UserSerializer(user)
        expected_data = {
            "id": user.id,
            "username": "testuser",
            "email": "testuser@example.com",
            "first_name": "Test",
            "last_name": "User",
        }
        self.assertEqual(serializer.data, expected_data)


class ClientSerializerTest(TestCase):
    def test_client_serializer_create(self):
        user_data = {
            "username": "clientuser",
            "email": "clientuser@example.com",
            "first_name": "Client",
            "last_name": "User",
        }
        client_data = {"phone": "123456789", "user": user_data}
        serializer = ClientSerializer(data=client_data)
        self.assertTrue(serializer.is_valid())
        client = serializer.save()

        self.assertEqual(client.phone, "123456789")
        self.assertEqual(client.user.username, "clientuser")
        self.assertEqual(client.user.email, "clientuser@example.com")

    def test_client_serializer_update(self):
        user = User.objects.create(
            username="clientuser", email="clientuser@example.com"
        )
        client = Client.objects.create(user=user, phone="123456789")
        update_data = {
            "phone": "987654321",
            "user": {"username": "updateduser", "email": "updateduser@example.com"},
        }
        serializer = ClientSerializer(instance=client, data=update_data)
        self.assertTrue(serializer.is_valid())
        updated_client = serializer.save()

        self.assertEqual(updated_client.phone, "987654321")
        self.assertEqual(updated_client.user.username, "updateduser")
        self.assertEqual(updated_client.user.email, "updateduser@example.com")


class TeamSerializerTest(TestCase):
    def test_team_serializer(self):
        user1 = User.objects.create(username="user1", email="user1@example.com")
        user2 = User.objects.create(username="user2", email="user2@example.com")
        team = Team.objects.create(name="Team A")
        team.users.add(user1, user2)

        serializer = TeamSerializer(team)
        expected_data = {
            "id": team.id,
            "name": "Team A",
            "users": [user1.id, user2.id],
            "user_names": [user1.id, user2.id],
        }
        self.assertEqual(serializer.data, expected_data)


class ProjectSerializerTest(TestCase):
    def test_project_serializer(self):
        user = User.objects.create(username="clientuser", email="client@example.com")
        client = Client.objects.create(user=user, phone="123456789")
        team = Team.objects.create(name="Team A")
        project = Project.objects.create(
            name="Project A",
            client=client,
            team=team,
            status="OPEN",
            start_date="2024-12-01",
            end_date="2024-12-31",
        )

        serializer = ProjectSerializer(project)
        expected_data = {
            "id": project.id,
            "name": "Project A",
            "client": client.id,
            "client_name": "clientuser",
            "team": team.id,
            "team_name": "Team A",
            "status": "OPEN",
            "start_date": "2024-12-01",
            "end_date": "2024-12-31",
        }
        self.assertEqual(serializer.data, expected_data)


class TaskSerializerTest(TestCase):
    def test_task_serializer(self):
        
        user = User.objects.create(username="clientuser", email="client@example.com")
        client = Client.objects.create(user=user, phone="123456789")
        team = Team.objects.create(name="Team A")
        project = Project.objects.create(
            name="Project A",
            client=client,
            team=team,
            status="OPEN",
            start_date="2024-12-01",
            end_date="2024-12-31",
        )
        task = Task.objects.create(
            name="Task A",
            description="Description A",
            project=project,
            status="PENDING",
        )

        
        serializer = TaskSerializer(task)
        serialized_data = serializer.data

        
        expected_data = {
            "id": task.id,
            "name": "Task A",
            "description": "Description A",
            "project": project.id,
            "project_name": "Project A",
            "status": "PENDING",
            "created_at": task.created_at.isoformat().replace("+00:00", "Z"),  
        }

        
        self.assertDictEqual(serialized_data, expected_data)