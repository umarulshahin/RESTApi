# Generated by Django 5.0.6 on 2024-05-22 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_team_people_team_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='team_name',
            new_name='team',
        ),
    ]
