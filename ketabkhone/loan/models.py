from django.db import models
# from secrets import choice
# from accounting.models import customuser


class Loan(models.Model):
    CHOICES = [
        ('C', 'Chosing'),
        ('S', 'Started'),
        ('R', 'Reterned'),
        ('T', 'To be reterned'),
    ]

    user = models.ForeignKey("accounting.CustomUser",
                             on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=CHOICES, max_length=35)
    def __str__ (self):
      return str(self.status)
    


class Debt(models.Model):
    amount = models.PositiveIntegerField()
    def __str__(self):
        return str(self.amount)
