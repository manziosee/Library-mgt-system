from django.db import models
# from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import User
# User = get_user_model()
# Create your models here.

class UserManager(BaseUserManager):
    def create_superuser(self, email, user_id, username, password=None,**extra_fields):

        user = self.create_user(email=self.normalize_email(email), user_id=user_id, username=username, password=password)
        user.is_active = True
        user.is_librarian = True
        user.is_admin = True
        user.is_staff = True
        # user.usertype = user.user_type[0][0]
        user.save(using=self.db)
        return user

    def create_user(self, email, user_id, username, password=None, **extra_fields ):
        # if not user_id:
        #     return ValueError("Users must have id!!")

        user = self.model(email=self.normalize_email(email), user_id=user_id, username=username, password=password)
        user.set_password(password)
        user.is_staff = True
        user.usertype = user.user_type[1][0]
        user.save(using=self.db)
        return user


class Library_user(AbstractUser):
    user_type = [
        ('librarian', 'Librarian'),
        ('student', 'Student')
    ]

    username = models.CharField(max_length=50, unique=True)
    usertype = models.CharField(choices= user_type, max_length=50, default = 'Student')
    email = models.CharField(max_length=50, unique=True)
    user_id = models.IntegerField(unique=True, default = 1)
    USERNAME_FIELD = 'user_id'
    REQUIRED_FIELDS = ['username']
    is_active = models.BooleanField(default=False)
    is_librarian = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    objects = UserManager()
    

    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self,perm):
        return True    


    @property
    def is_staff(self):
        return self.is_staff
    
    @property
    def is_admin(self):
        return self.is_admin

# class Student(models.Model):
#     user=models.OneToOneField(User, on_delete = models.CASCADE)
#     librarycard = models.IntegerField()
#     is_staff = models.BooleanField(default=True)