# Generated by Django 4.1.2 on 2022-11-15 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_student_create_on_student_modifield_on'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='create_on',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='modifield_on',
            new_name='modified_on',
        ),
    ]
