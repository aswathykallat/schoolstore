# Generated by Django 3.1.5 on 2022-11-10 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolstoreapp', '0005_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='email',
        ),
    ]
