from django.db import models

# Create your models here.

class AppUser(models.Model):
    first_name = models.CharField(max_length=50, null=False)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(null=False, unique=True)
    contact = models.CharField(null=False, unique=True, max_length=10)

    class Meta:
        db_table = "app_users"