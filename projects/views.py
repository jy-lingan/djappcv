from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Project
from .forms import ProjectForm

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Full-stack web development',
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This is my portfolio website',
    },
    {
        'id': '3',
        'title': 'Blog Website',
        'description': 'This is my blog website',
    }
]


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = Project.objects.get(id=pk)
    return render(request, 'projects/single-projects.html', {'project': projectObj})


def createProject(request):
    form = ProjectForm()

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form': form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project}
    return render(request, 'projects/delete_template.html', context)
