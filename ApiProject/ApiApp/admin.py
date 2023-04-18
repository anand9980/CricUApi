from django.contrib import admin

from ApiApp.models import Member, players, player_record, points_table, employee, Role, Department, P_table, table, \
    IPL_Teams
from ApiApp.views import IPL_Points_Table

# Register your models here.
admin.site.register(Member)
admin.site.register(players)
admin.site.register(player_record)
admin.site.register(points_table)
admin.site.register(employee)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(P_table)
admin.site.register(table)
admin.site.register(IPL_Teams)


