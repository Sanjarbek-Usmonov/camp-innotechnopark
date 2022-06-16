from django.shortcuts import redirect, render
from dashboard.person.forms import PersonForm
from blog.models import Person


def person_list_detail_delete(requests, pk=None, delete=None):
    ctx = {}
    if pk:
        html = 'dashboard/person/details.html'
        ctx['person'] = Person.objects.get(pk=pk)
    elif delete:
        Person.objects.get(pk=delete).delete()
        return redirect('person_list')
    else:
        html = 'dashboard/person/list.html'
        ctx['person'] = Person.objects.all()
    return render(requests, html, ctx)


def person_add_edit(requests, pk=None):
    if pk:
        root = Person.objects.get(pk=pk)
    else:
        root = None
    form = PersonForm(instance=root)

    if requests.POST:
        forms = PersonForm(requests.POST, requests.FILES, instance=root)
        if forms.is_valid():
            forms.save()
            return redirect('person_list')
    ctx = {
        'form': form
    }
    return render(requests, 'dashboard/person/forms.html', ctx)
