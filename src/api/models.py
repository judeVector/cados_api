from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=120)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.name


class Advocate(models.Model):
    username = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)
    bio = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.username
