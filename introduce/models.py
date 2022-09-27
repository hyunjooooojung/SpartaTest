from django.db import models

# Create your models here.
class AccessLog(models.Model):
    db_table = "AccessLog"

    created_at = models.DateTimeField("접속시간", auto_now_add=True)
    location = models.CharField("접속 경로", max_length=50)
