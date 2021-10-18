from django.contrib import admin
from .models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_Name','uploaded_By','date',)

admin.site.register(Project, ProjectAdmin)