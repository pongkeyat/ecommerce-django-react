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
    
    username = models.CharField(max_length = 15, blank = True, null =True)
    role = models.CharField(max_length = 20, choices= ROLE_CHOICES, default = "customer", help_text ="Role of the user")

    # use email as the unique identifier for authentication
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    #methods

    def __str__(self):
        # username may be blank/null; fall back to email
        display = self.username if self.username else self.email
        return f"{display} ({self.role})"
    
    
    def is_vendor(self):
        return self.role == "vendor"
    
    def is_customer(self):
        return self.role == "customer"

