from django.shortcuts import render
from .models import Project, ProjectMedia


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)


def project_detail(request, project_id):
    project = Project.objects.get(pk=project_id)
    media = ProjectMedia.objects.filter(project=project)

    context = {
            'project': project,
            'media': media,
            }
    return render(request, 'projects/project_detail.html', context)
