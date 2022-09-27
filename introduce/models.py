from django.db import models

# Create your models here.
class UserModel(models.Model):
    class AccessLog:
        db_table = "AccessLog"

        created_at = models.DateTimeField(auto_now_add=True)
        location = models.CharField(max_length=256, null=False)
