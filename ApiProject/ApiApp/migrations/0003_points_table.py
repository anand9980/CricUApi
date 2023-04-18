# Generated by Django 4.1.7 on 2023-04-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ApiApp', '0002_player_record_players'),
    ]

    operations = [
        migrations.CreateModel(
            name='points_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamName', models.CharField(max_length=100)),
                ('matches', models.IntegerField(max_length=100)),
                ('win', models.IntegerField(max_length=100)),
                ('lost', models.IntegerField(max_length=100)),
                ('RunRate', models.IntegerField(max_length=100)),
            ],
        ),
    ]