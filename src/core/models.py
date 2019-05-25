from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    
    def create_user(self,email,password=None,**kwargs):
        """Creates and Saves a new User"""
        if not email:
            raise ValueError("User must have an Email Address")
        user = self.model(email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,password):
        """Create a new SuperUser"""
        user = self.create_user(email=email,password=password)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser,PermissionsMixin):

    """Custom User Model that supports email instead of Username"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'