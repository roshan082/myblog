from datetime import datetime
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

class BlogAppUser(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15,null=True)
    password = models.CharField(max_length=20)
    profile_image = models.FileField(upload_to='images/profile_images/', null=True)
    verification_code = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at =models.DateTimeField(default=datetime.now(), blank=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    removed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "app_blogusers"

class BlogCategory(models.Model):
    category = models.CharField(max_length=100)
    parent_id = models.BigIntegerField(null=True)

    class Meta:
        db_table = "app_blogcategories"

class BlogPost(models.Model):
    post_title = models.CharField(max_length=200)
    post_description = models.TextField(max_length=500)
    slug = models.CharField(max_length=200)
    caregory_id = models.BigIntegerField(null=True)
    post_image = models.FileField(upload_to='images/blog_posts/')
    user_id = models.BigIntegerField(null=True)
    post_status = models.CharField(null=True, max_length=20)
    created_at =models.DateTimeField(default=datetime.now(), blank=False)
    updated_at = models.DateTimeField(null=True, blank=True)
    removed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "app_blogposts"

