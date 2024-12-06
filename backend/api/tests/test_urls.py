from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from api.views import ClientViewSet, ProjectViewSet, TaskViewSet, TeamViewSet, UserViewSet


class URLResolutionTest(SimpleTestCase):
    def test_clients_url(self):
        url = reverse('client-list')  
        self.assertEqual(resolve(url).func.cls, ClientViewSet)

    def test_projects_url(self):
        url = reverse('project-list')  
        self.assertEqual(resolve(url).func.cls, ProjectViewSet)

    def test_tasks_url(self):
        url = reverse('task-list')  
        self.assertEqual(resolve(url).func.cls, TaskViewSet)

    def test_teams_url(self):
        url = reverse('team-list')  
        self.assertEqual(resolve(url).func.cls, TeamViewSet)

    def test_users_url(self):
        url = reverse('user-list')  
        self.assertEqual(resolve(url).func.cls, UserViewSet)

    def test_project_tasks_url(self):
        project_id = 1
        url = reverse('project-tasks', kwargs={'project_id': project_id})
        self.assertEqual(resolve(url).func.cls, TaskViewSet)


class URLIntegrationTest(APITestCase):
    def test_clients_endpoint(self):
        url = reverse('client-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_projects_endpoint(self):
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_tasks_endpoint(self):
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_teams_endpoint(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_users_endpoint(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_project_tasks_endpoint(self):
        project_id = 1
        url = reverse('project-tasks', kwargs={'project_id': project_id})
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 404])  
