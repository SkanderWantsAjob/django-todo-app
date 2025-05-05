from django.db import models
from django.contrib.auth.models import User

class TODOO(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        DONE = 'DONE', 'Done'
        NOT_DONE = 'NOT_DONE', 'Not Done'
    srno=models.AutoField(primary_key=True, auto_created=True)
    title=models.CharField(max_length=25)
    date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NOT_DONE
    )
    
    
    def __str__(self):
        return f"{self.title} - {self.status}"

