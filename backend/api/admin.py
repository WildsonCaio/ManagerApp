from django.contrib import admin
from .models import *

admin.site.register(Client)
admin.site.register(Task)
admin.site.register(Project)
admin.site.register(Team)
