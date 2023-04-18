from django.contrib.sessions.backends import db
from django.db.backends import mysql
import mysql.connector
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.template import loader
from .models import employee, Department, Role, P_table, table, IPL_Teams
from datetime import datetime


def index(request):
    return render(request, 'index.html')


def all_players(request):
    name = request.POST.get('name')
    test = mysql.connector.connect(host="localhost",
                                   user="root", password="995099",
                                   database="API")
    crs = test.cursor()
    # query = "Select * from apiapp_players where id = " + id
    query = "select * from apiapp_players"
    # query = "select * from apiapp_players  where id=1 union select * from apiapp_player_record where id=1"
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['massage'] = 'player not found'
    else:
        for l in data:
            d = {}
            d['player_id'] = l[0]
            d['player_name'] = l[1]
            d['age'] = l[2]
            d['country'] = l[3]
            d['ipl_team'] = l[4]
            d['Ranking'] = l[5]
            list.append(d)
        dict['players'] = list
    return JsonResponse(dict)


def player_details(request, id):
    name = request.POST.get('name')
    test = mysql.connector.connect(host="localhost",
                                   user="root", password="995099",
                                   database="API")
    crs = test.cursor()
    query = "Select * from apiapp_players where id = " + id
    # query = "select * from apiapp_players"
    # query = "select * from apiapp_players  where id=1 union select * from apiapp_player_record where id=1"
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['massage'] = 'player not found'
    else:
        for l in data:
            d = {}
            d['player_id'] = l[0]
            d['player_name'] = l[1]
            d['age'] = l[2]
            d['country'] = l[3]
            d['ipl_team'] = l[4]
            d['Ranking'] = l[5]
            list.append(d)
        dict['players'] = list
    return JsonResponse(dict)


def IPL_Points_Table(request):
    test = mysql.connector.connect(host="localhost",
                                   user="root", password="995099",
                                   database="API")
    crs = test.cursor()
    query = "select * from apiapp_points_table"
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['massage'] = 'empty'
    else:
        for l in data:
            d = {}
            d['Ranking'] = l[0]
            d['team_name'] = l[1]
            d['matches'] = l[2]
            d['win'] = l[3]
            d['lost'] = l[4]
            d['RunRate'] = l[5]
            list.append(d)
        dict['points table'] = list
    return JsonResponse(dict)


def all_emp(request):
    emps = employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'all_emp.html', context)


def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        salary = int(request.POST['salary'])
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = employee(first_name=first_name, last_name=last_name, salary=salary, bonus=bonus, phone=phone,
                           dept_id=dept,
                           role_id=role, hire_date=datetime.now())
        new_emp.save()
        return HttpResponse('employee added successful')
    elif request.method == 'GET':

        return render(request, 'add_emp.html')
    else:
        return HttpResponse('error')


def remove_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_remove = employee.objects.get(id=emp_id)
            emp_remove.delete()
            return HttpResponse('removed successfully')
        except:
            return HttpResponse('enter correct employee id')
    emps = employee.objects.all()
    context = {
        'emps': emps
    }

    return render(request, 'remove_emp.html', context)


def filter_emp(request):
    return render(request, 'filter.html')


def P_table(request):
    test = mysql.connector.connect(host="localhost",
                                   user="root", password="995099",
                                   database="API")
    crs = test.cursor()
    query = 'select * from apiapp_p_table'
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['massage'] = 'player not found'
    else:
        for l in data:
            d = {}
            d['Ranking'] = l[0]
            d['team_name'] = l[1]
            d['matches'] = l[2]
            d['win'] = l[3]
            d['lost'] = l[4]
            d['NRR'] = l[5]
            d['points'] = l[6]
            list.append(d)
        dict['points table'] = list
    return JsonResponse(dict)


def Table(request):
    data = table.objects.all()
    context = {
        'tp': data
    }
    print(context)
    return render(request, 'P_table.html', context)


def teams(request):
    data = IPL_Teams.objects.all()
    context = {
        'team': data
    }
    print(context)
    return render(request, 'teams.html', context)


def team2(request):
    test = mysql.connector.connect(host="localhost",
                                   user="root", password="995099",
                                   database="API")
    crs = test.cursor()
    query = "select * from apiapp_ipl_teams;"
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['massage'] = 'error'
    else:
        for l in data:
            d = {}
            d['id'] = l[0]
            d['team_name'] = l[1]

            list.append(d)
        dict['points table'] = list
    return JsonResponse(dict)



