from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f'Name: {self.name}, email: {self.email}, age: {self.age}'
    
# Create your models here.
