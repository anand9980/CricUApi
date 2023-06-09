# Generated by Django 4.1.7 on 2023-04-06 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0004_department_role_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='P_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('matches', models.IntegerField(max_length=100)),
                ('win', models.IntegerField(default=0)),
                ('lost', models.IntegerField(default=0)),
                ('NRR', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
    ]
