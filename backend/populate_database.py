import os
import django
from datetime import date  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')  
django.setup()

from django.contrib.auth.models import User
from api.models import Client, Project, Team, Task  

def populate_database():
     
        users_data = [
            {"username": "santander_user", "email": "santander@example.com"},
            {"username": "bradesco_user", "email": "bradesco@example.com"},
            {"username": "caixa_user", "email": "caixa@example.com"},
        ]

        users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(**user_data)
            if created:
                user.set_password("password123")  
                user.save()
            users.append(user)
            print(f"Usuário {'criado' if created else 'existente'}: {user.username}")

        
        clients_data = [
            {"user": users[0], "phone": "123456789"},
            {"user": users[1], "phone": "987654321"},
            {"user": users[2], "phone": "555555555"},
        ]

        clients = []
        for client_data in clients_data:
            client, created = Client.objects.get_or_create(**client_data)
            clients.append(client)
            print(f"Cliente {'criado' if created else 'existente'}: {client}")

        
        teams_data = [
            {"name": "DEV"},
            {"name": "INFRA"},
            {"name": "SUPORTE"},
        ]

        teams = []
        for team_data in teams_data:
            team, created = Team.objects.get_or_create(**team_data)
            team.users.set(users)  
            teams.append(team)
            print(f"Equipe {'criada' if created else 'existente'}: {team}")

        
        projects_data = [
            {"name": "Sistema de emissão de NF", "client": clients[0], "team": teams[0], "status": "IN_EXECUTION", "start_date": date(2023, 1, 1), "end_date": date(2023, 6, 30)},
            {"name": "Sistema de tráfego de arquivos", "client": clients[1], "team": teams[1], "status": "PENDING", "start_date": date(2023, 7, 1), "end_date": date(2023, 12, 31)},
            {"name": "Migração de legado", "client": clients[2], "team": teams[2], "status": "COMPLETED", "start_date": date(2022, 5, 1), "end_date": date(2022, 12, 31)},
        ]

        projects = []
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(**project_data)
            projects.append(project)
            print(f"Projeto {'criado' if created else 'existente'}: {project}")

        
        tasks_data = [
            {"name": "Configurar ambiente", "description": "Configurar o ambiente inicial do projeto", "project": projects[0], "status": "PENDING"},
            {"name": "Desenvolver módulo de login", "description": "Criar o sistema de login do usuário", "project": projects[0], "status": "IN_EXECUTION"},
            {"name": "Realizar testes de carga", "description": "Testar o desempenho do sistema", "project": projects[1], "status": "PENDING"},
            {"name": "Documentação final", "description": "Gerar a documentação final do sistema", "project": projects[2], "status": "COMPLETED"},
        ]

        for task_data in tasks_data:
            task, created = Task.objects.get_or_create(**task_data)
            print(f"Tarefa {'criada' if created else 'existente'}: {task}")

        print("População do banco de dados concluída com sucesso.")

if __name__ == "__main__":
    populate_database()
