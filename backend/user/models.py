from django.db import models
from django.contrib.auth.models import AbstractUser
from restaurant.models import Restaurant


class User(AbstractUser):
    email = models.EmailField(unique=True)
    cpf = models.CharField(max_length=14, unique=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=True)
    user_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "cpf"
    REQUIRED_FIELDS = ["email"]
 
    class Meta:
        db_table = 'user' 
        managed = True 
        verbose_name = 'user'
        verbose_name_plural = 'users' 
        
    def __str__(self):
        return self.cpf