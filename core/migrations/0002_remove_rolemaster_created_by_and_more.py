# Generated by Django 5.2 on 2025-04-29 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rolemaster',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='rolemaster',
            name='modified_by',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
        migrations.DeleteModel(
            name='RoleMaster',
        ),
    ]
