from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "PMS/index.html", {
        'projects': projects
    })

def AddProjects(request):
    project = Project.objects.all()
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project has been Added!")
            return redirect('projects')
        else:
            messages.success(request, "Project could not be Added!")
            return redirect('projects')
    return render(request,'PMS/project.html',{'addproject':project,'form':form})

def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if project.delete():
        messages.success(request, "Project has been Deleted!")
        return redirect('projects')
    else:
        messages.success(request, "Project could not be Deleted!")
        return redirect('projects')

def updateProject(request, pk):
    projectUpdate = Project.objects.get(id=pk)
    updateForm = ProjectForm(instance=projectUpdate)
    if request.method == 'POST':
        updateForm = ProjectForm(request.POST, instance=projectUpdate)
        if updateForm.is_valid():
            updateForm.save()
            messages.success(request, "Project has been Updated!")
            return redirect('projects')
        else:
            messages.success(request, "Project failed to Update!")
            return redirect('projects')
    return render(request,'PMS/updateProject.html',{'project':projectUpdate,'updateform':updateForm})