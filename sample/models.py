from django.db import models

class Student(models.Model):
    u_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=100,default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
class User(models.Model):
    u_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,default=True)
    otp = models.IntegerField(default=0)
    v_status = models.IntegerField(default=0)
    password = models.CharField(max_length=100)