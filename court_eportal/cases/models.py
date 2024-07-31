# cases/models.py

from django.db import models

from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

class Case(models.Model):
    case_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_filed = models.DateField()
    status = models.CharField(max_length=50)
    plaintiff = models.CharField(max_length=200, default="Unknown Plaintiff")
    defendant = models.CharField(max_length=200, default="Unknown Defendant")

    def clean(self):
        super().clean()
        if self.date_filed and self.date_filed > date.today():
            raise ValidationError('The date filed cannot be in the future.')

    def __str__(self):
        return self.case_number


class Hearing(models.Model):
    case = models.ForeignKey(Case, related_name='hearings', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Hearing for {self.case.case_number} on {self.date}"
