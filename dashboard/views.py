from django.shortcuts import render

# Create your views here.


def admin_index(requests):
    return render(requests, 'dashboard/admin-index.html')


# def ctg_list(requests):
#     return render(requests, 'dashboard/category/list.html')
#
#
# def person_list(requests):
#     return render(requests, 'dashboard/person/list.html')
#
#
# def project_list(requests):
#     return render(requests, 'dashboard/project/list.html')