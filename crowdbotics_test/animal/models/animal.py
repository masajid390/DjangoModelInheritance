from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=255)
    birthday = models.DateTimeField()
