from django.db import models

class Case(models.Model):
    case_number = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_filed = models.DateField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.case_number

class Hearing(models.Model):
    case = models.ForeignKey(Case, related_name='hearings', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Hearing for {self.case.case_number} on {self.date}"
