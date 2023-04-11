from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from rest_framework.authtoken.models import Token
from django.utils import timezone

class UserManager(BaseUserManager):
    '''Custom user model'''
    def create_user(self, email,  name, lastname,region, password=None):
        '''Creates default user'''


        
        if not email:
            raise ValueError('Email is required')
        
        email = self.normalize_email(email)
        user = self.model(email = email, name = name, lastname = lastname, region = region)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, name, lastname, region, password):
        '''Creates superuser'''
        user = self.create_user(email, name, lastname,region, password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using = self._db)
        return user

    def create_token(self, user):
        token = Token.objects.create(user=user)
        token.created = timezone.now()
        token.token_expiry = timezone.now() + timedelta(hours=24)
        token.save()
        return token

class User(AbstractBaseUser, PermissionsMixin):
    '''Represents users database'''
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    region = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    token_expiry = models.DateTimeField(null=True, blank=True)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'lastname', 'region']

    def renew_token(self, expires_in):
        self.token_expiry = timezone.now() + timezone.timedelta(seconds=expires_in)
        self.save()

    def get_full_name(self):
        '''Returns full name'''
        return '{0} {1}'.format(self.name, self.lastname)

    
    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.email


