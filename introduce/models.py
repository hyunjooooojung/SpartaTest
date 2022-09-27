from django.db import models

# Create your models here.
class AccessLog(models.Model):
    

    created_at = models.DateTimeField("접속 시간 : ", auto_now_add=True)
    location = models.CharField("접속 경로 : ", max_length=50)

    def __str__(self):
        return f"{self.created_at} / {self.location}"