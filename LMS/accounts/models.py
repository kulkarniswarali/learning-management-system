from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from courses.models import *
# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Change this to a unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='customuser'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Change this to a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='customuser'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def get_username(self):
        return self.email
    

class Profile(models.Model):

    CAT = (
        ('Student', 'Student'),
        ('Instructor', 'Instructor')
    )
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE ,null=True, blank=True)
    category = models.CharField(max_length=200,choices=CAT, null=True, blank=True)
    field = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.FileField(upload_to='files', null=True, blank=True)
    
    def __str__(self):
        return  f"{self.user.first_name}"
    
