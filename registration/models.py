from django.db import models

# Create your models here.
class Person(models.Model):
  # Personal Info
  name = models.CharField(max_length=50)
  age_group = models.CharField(max_length=10)

  # Personal requirements
  dietary_restrictions = models.TextField(max_length=200)

  # Church affiliations
  affiliation = models.CharField(max_length=3, choices=[('CC','zhongwentang'), ('OIF', 'OIF')])
  small_group = models.CharField(max_length=10, choices=[('Oasis', 'Oasis')])
