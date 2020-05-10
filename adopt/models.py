from django.db import models


class Pet(models.Model):
    CHOICES = (
            ('red', 'Red'),
            ('yellow', 'Yellow'),
            ('black', 'Black'),
    )
    name = models.CharField('Name', max_length=50)  # first column

    age = models.IntegerField('Age')

    color = models.CharField('Color', max_length=50, choices=CHOICES)
# Create your models here.
