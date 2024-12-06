from django.test import TestCase
from django.contrib.auth.models import User
from api.models import Client, Team, Project, Task


class ClientModelTest(TestCase):
    def test_client_creation(self):
        user = User.objects.create(username="clientuser", email="client@example.com")
        client = Client.objects.create(user=user, phone="123456789")
        self.assertEqual(client.user.username, "clientuser")
        self.assertEqual(client.phone, "123456789")
        self.assertEqual(str(client), "clientuser")


class TeamModelTest(TestCase):
    def test_team_creation(self):
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        team = Team.objects.create(name="Team A")
        team.users.add(user1, user2)
        self.assertEqual(team.name, "Team A")
        self.assertEqual(team.users.count(), 2)
        self.assertEqual(str(team), "Team A")


class ProjectModelTest(TestCase):
    def test_project_creation(self):
        user = User.objects.create(username="clientuser", email="client@example.com")
        client = Client.objects.create(user=user, phone="123456789")
        team = Team.objects.create(name="Team A")
        project = Project.objects.create(
            name="Project A",
            client=client,
            team=team,
            status="PENDING",
            start_date="2024-12-01",
            end_date="2024-12-31",
        )
        self.assertEqual(project.name, "Project A")
        self.assertEqual(project.client.user.username, "clientuser")
        self.assertEqual(project.team.name, "Team A")
        self.assertEqual(project.status, "PENDING")
        self.assertEqual(str(project), "Project A")


class TaskModelTest(TestCase):
    def test_task_creation(self):
        user = User.objects.create(username="clientuser", email="client@example.com")
        client = Client.objects.create(user=user, phone="123456789")
        team = Team.objects.create(name="Team A")
        project = Project.objects.create(
            name="Project A",
            client=client,
            team=team,
            status="PENDING",
            start_date="2024-12-01",
            end_date="2024-12-31",
        )
        task = Task.objects.create(
            name="Task A",
            description="Description A",
            project=project,
            status="PENDING",
        )
        self.assertEqual(task.name, "Task A")
        self.assertEqual(task.description, "Description A")
        self.assertEqual(task.project.name, "Project A")
        self.assertEqual(task.status, "PENDING")
        self.assertEqual(str(task), "Task A")
