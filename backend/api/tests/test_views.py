from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from api.models import Client, Project, Task, Team


class UserViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser", email="testuser@example.com")

    def test_list_users(self):
        response = self.client.get('/api/v1/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get('results', [])
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['username'], self.user.username)

    def test_create_user(self):
        data = {"username": "newuser", "email": "newuser@example.com"}
        response = self.client.post('/api/v1/users/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['username'], data['username'])


class ClientViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="clientuser", email="client@example.com")
        self.client_obj = Client.objects.create(user=self.user, phone="123456789")

    def test_list_clients(self):
        response = self.client.get('/api/v1/clients/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get('results', [])
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['user']['username'], self.user.username)



class TeamViewSetTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(username="teamuser1", email="teamuser1@example.com")
        self.user2 = User.objects.create(username="teamuser2", email="teamuser2@example.com")
        self.team = Team.objects.create(name="Team Alpha")
        self.team.users.add(self.user1, self.user2)

    def test_list_teams(self):
        response = self.client.get('/api/v1/teams/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get('results', [])
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['name'], self.team.name)

    def test_create_team(self):
        data = {"name": "Team Beta", "users": [self.user1.id, self.user2.id]}
        response = self.client.post('/api/v1/teams/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], data['name'])


class ProjectViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="clientuser", email="client@example.com")
        self.client_obj = Client.objects.create(user=self.user, phone="123456789")
        self.team = Team.objects.create(name="Team Alpha")
        self.project = Project.objects.create(
            name="Test Project",
            client=self.client_obj,
            team=self.team,
            status="OPEN",
            start_date="2024-12-01",
            end_date="2024-12-31"
        )

    def test_list_projects(self):
        response = self.client.get('/api/v1/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get('results', [])
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['name'], self.project.name)



class TaskViewSetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="clientuser", email="client@example.com")
        self.client_obj = Client.objects.create(user=self.user, phone="123456789")
        self.team = Team.objects.create(name="Team Alpha")
        self.project = Project.objects.create(
            name="Test Project",
            client=self.client_obj,
            team=self.team,
            status="OPEN",
            start_date="2024-12-01",
            end_date="2024-12-31"
        )
        self.task = Task.objects.create(
            name="Test Task",
            description="Task Description",
            project=self.project,
            status="PENDING"
        )

    def test_list_tasks(self):
        response = self.client.get('/api/v1/tasks/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get('results', [])
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['name'], self.task.name)

    def test_create_task(self):
        data = {
            "name": "New Task",
            "description": "New Task Description",
            "project": self.project.id,
            "status": "PENDING"
        }
        response = self.client.post('/api/v1/tasks/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['name'], data['name'])

    def test_filter_tasks_by_status(self):
        response = self.client.get(f'/api/v1/tasks/?status=PENDING')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get('results', [])
        self.assertTrue(len(results) > 0)
        self.assertEqual(results[0]['status'], 'PENDING')
