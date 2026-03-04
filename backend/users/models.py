from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    #Roles
    ROLE_CHOICES = (
        ("vendor", "Vendor"),
        ("customer", "Customer")
    )
    #fields
    email = models.EmailField(unique = True)
    username = moels.CharField(max_length = 15, blank = True, null =True)
    role = models.CharField(max_length = 20, choice= ROLE_CHOICES, default = "customer", help_text ="Role of the user")

    created_at = model.DateTimeField(auto_now_add = True)
    updated_at = model.DateTimeField(auto_now_add = True)

    #methods

    def __str__(self):
        return  f"{self.username} ({self.role})"
    
    
    def is_(self):
        return self.role == "vendor"
    
    def is_admin(self):
        return self.role == "customer"

