from django.shortcuts import render
from .models import Project, ProjectMedia


def projects(request):
    projects = Project.objects.all()
    media = ProjectMedia.objects.all()


    context = {'projects': projects, 'media':media}
    return render(request, 'projects/projects.html', context)
