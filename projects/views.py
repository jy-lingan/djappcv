from django.http import HttpResponse
from django.shortcuts import render

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
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObject = None
    for i in projectsList:
        if i['id'] == pk:
            projectObject = i
    return render(request, 'projects/single-projects.html', {'project': projectObject})
