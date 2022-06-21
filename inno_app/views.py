from django.shortcuts import render
from django.views.generic import CreateView

from .models import Info
# Create your views here.


def index_ru(requests):
    info = Info()
    if requests.POST:
        info.full_name = requests.POST.get('full_name', '')
        info.phone = requests.POST.get('phone', '')
        info.date = requests.POST.get('date', '')
        info.save()
    return render(requests, 'index_ru.html', {'info': info})


def index(requests):
    info = Info()
    if requests.POST:
        info.full_name = requests.POST.get('full_name', '')
        info.phone = requests.POST.get('phone', '')
        info.date = requests.POST.get('date', '')
        info.save()
    return render(requests, 'index.html',  {'info': info})



import csv

# from django.http import HttpResponse
# from django.contrib.auth.models import User
#
#
# def export_users_csv(request):
#     response = HttpResponse(content_type='text/csv')
#     response['Content-Disposition'] = 'attachment; filename="info.csv"'
#
#     writer = csv.writer(response)
#     writer.writerow(['Full name', 'Phone', 'Date'])
#
#     users = Info.objects.all().values_list('full_name', 'phone', 'date')
#     for user in users:
#         writer.writerow(user)
#
#     return response


import xlwt
from django.http import HttpResponse

def export_users_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Info.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Info')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Full name', 'Phone', 'Date']

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = Info.objects.all().values_list('full_name', 'phone', 'date')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response