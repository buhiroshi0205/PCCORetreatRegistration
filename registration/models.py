from django.db import models

# Create your models here.
class Person(models.Model):
  # Names
  english_first_name = models.CharField(max_length=50)
  english_last_name = models.CharField(max_length=50)
  chinese_name = models.CharField(max_length=10)

  # Price group
  age = models.IntegerField()
  status = models.CharField(max_length=50, choices=[('Student', 'Student'),('Non-student', 'Non-student')])

  # Personal requirements
  allergies = models.TextField(max_length=200)
  dietary_restrictions = models.TextField(max_length=200)

  # Emergency Contact
  emergency_contact = models.CharField(max_length=12)

  # Church affiliations
  # affiliation = models.CharField(max_length=3, choices=[('CC','zhongwentang'), ('OIF', 'OIF')])


class Registration(models.Model):
  representative = models.ForeignKey(Person, on_delete=models.PROTECT)
  small_group = models.CharField(max_length=10, choices=[('Oasis', 'Oasis')])
  email = models.CharField(max_length=50)
