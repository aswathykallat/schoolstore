from django.db import models


class student(models.Model):
    username=models.CharField(max_length=200,null=True)
   
    password=models.CharField(max_length=200,null=True)
    password2=models.CharField(max_length=200,null=True)


class req(models.Model):
    name=models.CharField(max_length=200,null=True)
    dob=models.CharField(max_length=200,null=True)
    age=models.CharField(max_length=200,null=True)
    gender=models.CharField(max_length=200,null=True)
    no=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    add=models.CharField(max_length=200,null=True)
    subject=models.CharField(max_length=200,null=True)
    topic=models.CharField(max_length=200,null=True)
    chapter=models.CharField(max_length=200,null=True)


