from django.db import models

class Lead(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.CharField(max_length=100, unique=True)
    message = models.CharField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ClassName(models.Model):
    name = models.CharField(max_length=100, blank=False)

class Students(models.Model):
    name = models.CharField(max_length=100, blank=False)
    on_class = models.BooleanField(default=False)
    classname = models.ForeignKey(ClassName, blank=True, null=True, on_delete=models.CASCADE)