# Generated by Django 3.1.5 on 2022-11-10 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolstoreapp', '0004_auto_20221109_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
