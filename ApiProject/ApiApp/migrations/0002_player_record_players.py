# Generated by Django 4.1.7 on 2023-04-04 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='player_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('runs', models.IntegerField(max_length=100000)),
                ('strike_Rate', models.BooleanField(max_length=100)),
                ('wickets', models.IntegerField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('ipl_team_name', models.CharField(max_length=100)),
                ('ranking', models.IntegerField(max_length=100)),
            ],
        ),
    ]
