from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.index, name='projects'),
    path('project/addproject/',views.AddProjects, name='add-project'),
    path('project/delete/<int:pk>/', views.deleteProject, name='delete-project'),
    path('project/updateproject/<int:pk>/', views.updateProject, name='update-project')
]