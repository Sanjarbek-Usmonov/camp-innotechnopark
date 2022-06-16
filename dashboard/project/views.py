from django.shortcuts import redirect, render
from dashboard.project.forms import ProjectForm
from blog.models import Project


def project_list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'dashboard/project/details.html'
        ctx['project'] = Project.objects.get(pk=pk)
    elif delete:
        Project.objects.get(pk=delete).delete()
        return redirect('project_list')
    else:
        html = 'dashboard/project/list.html'
        ctx['project'] = Project.objects.all()
    return render(requests, html, ctx)


def project_add_edit(requests, pk=None):
    if pk:
        root = Project.objects.get(pk=pk)
    else:
        root = None
    form = ProjectForm(instance=root)

    if requests.POST:
        forms = ProjectForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('project_list')
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/project/forms.html', ctx)
