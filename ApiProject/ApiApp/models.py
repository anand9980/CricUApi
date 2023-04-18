from django.db import models
from django.http import HttpResponse
from django.template import loader


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)


class players(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(max_length=100)
    country = models.CharField(max_length=100)
    ipl_team_name = models.CharField(max_length=100)
    ranking = models.IntegerField(max_length=100)


class player_record(models.Model):
    players.name = models.CharField(max_length=100)
    runs = models.IntegerField(max_length=100000)
    strike_Rate = models.BooleanField(max_length=100)
    wickets = models.IntegerField(max_length=1000)


class points_table(models.Model):
    teamName = models.CharField(max_length=100)
    matches = models.IntegerField(max_length=100)
    win = models.IntegerField(max_length=100)
    lost = models.IntegerField(max_length=100)
    RunRate = models.IntegerField(max_length=100)


class Department(models.Model):
    name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s " % (self.first_name, self.last_name, self.phone)


class P_table(models.Model):
    team_name = models.CharField(max_length=100, null=False)
    matches = models.IntegerField(max_length=100)
    win = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    NRR = models.IntegerField(default=0)
    points = models.IntegerField(default=0)


class table(models.Model):
    team_name = models.CharField(max_length=100, null=False)
    matches = models.IntegerField(max_length=100)
    win = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    NRR = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return " %s %s %s %s %s %s " % (self.team_name, self.matches, self.win, self.lost, self.NRR, self.points)


class IPL_Teams(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
