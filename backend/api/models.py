from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_profile')
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username
    
 

class Team(models.Model):
    name = models.CharField(max_length=255)
    users = models.ManyToManyField(User, related_name='user_team')

    def __str__(self):
        return self.name

    
    
class Project(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendng'),
        ('IN_EXECUTION', 'In Execution'),
        ('COMPLETED', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="projects")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="teams")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='OPEN')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_EXECUTION', 'In Execution'),
        ('COMPLETED', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks")
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
