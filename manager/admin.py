from django.contrib import admin
from .models import Skill, About, Project, Contact

# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(About)
admin.site.register(Contact)