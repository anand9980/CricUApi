from django.urls import path
from . import views
from .models import table
from .views import IPL_Points_Table, index, all_emp, add_emp, remove_emp, filter_emp, all_players, player_details, \
    P_table, Table, IPL_Teams, team2, teams


class Team2:
    pass


urlpatterns = [
    path('player/', all_players),
    path('player/<str:id>', player_details),
    path('Pt', IPL_Points_Table),
    path('p_table', P_table),
    path('t', Table),
    path('teams', teams),
    path('team2', team2),
    path('index', index),

    path('all_emp', all_emp),
    path('add_emp', add_emp),
    path('remove_emp', remove_emp),
    path('remove_emp/<int:emp_id>', remove_emp),
    path('filter_emp', filter_emp),

]
