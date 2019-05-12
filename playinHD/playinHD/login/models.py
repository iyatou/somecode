from django.db import models

# Create your models here.
class user(models.Model):
    AgentInfo_id=models.IntegerField(primary_key=True)
    userphone=models.CharField(max_length=50)
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
