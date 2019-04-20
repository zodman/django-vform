from django.db import models


class Name (models.Model):
    name = models.CharField(max_length=10)

class Address(models.Model):
    street = models.CharField(max_length=20)
    address_alternative = models.CharField(max_length=255)
    number = models.PositiveIntegerField()
    name = models.ForeignKey("Name", on_delete = models.CASCADE)

