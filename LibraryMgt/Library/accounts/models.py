from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, email, gender, password=None, **otherfields):
        user = self.model(email=self.normalize_email(email), gender=gender, password=password)
        user.set_password(password)
        user.is_active = False
        user.usertype = user.USER_TYPE[1][0]
        user.save(using=self.db)
        return user
        
    def create_superuser(self,email, gender, password=None, **otherfields):
        user = self.create_user(email=self.normalize_email(email), gender=gender, password=password)
        user.is_active = True
        user.is_admin = True
        user.staff = True
        user.usertype = user.USER_TYPE[0][0]
        user.save(using=self.db)
        return user

class MyUser(AbstractBaseUser):
    USER_TYPE=[
        ['librarian', 'Librarian'],
        ['student', 'Student'],
    ]
    GENDER=[
        ['female', 'Female'],
        ['male', 'Male'],
    ]


    email = models.CharField(unique=True, max_length=30)
    #username = models.CharField(unique=True, max_length=30)
    usertype = models.CharField(choices=USER_TYPE, max_length=20, default='Librarian')
    gender = models.CharField(choices= GENDER,max_length=10)
    REQUIRED_FIELDS = ['gender']
    USERNAME_FIELD = 'email'
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    objects = UserManager()

    def has_module_perms(self, app_label):
        return True
    
    def has_perm(self,perm):
        return True    

    @property
    def is_staff(self):
        return self.staff