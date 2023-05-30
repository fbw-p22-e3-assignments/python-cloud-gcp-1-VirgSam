from django.db import models


class Todo(models.Model):
    
    task = models.CharField(max_length=200, null=True, unique=True)
    details = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return self.name