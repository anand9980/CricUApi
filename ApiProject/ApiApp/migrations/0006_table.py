# Generated by Django 4.1.7 on 2023-04-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0005_p_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='table',
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