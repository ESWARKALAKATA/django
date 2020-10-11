from django.db import models

class Person(models.Model):
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
