import uuid

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Permission
# Create your models here.

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, username, name, email, password):

        user = self.model(
            username = username,
            name = name,
            email = self.normalize_email(email),
            password = password,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, name, email, password):

        user = self.model(
            username = username,
            name = name,
            email = self.normalize_email(email),
            password = password,
        )
        user.is_staff = True
        user.is_superuser = True

        user.set_password(password)
        user.save(using=self._db)

        return user

class Account(AbstractBaseUser, PermissionsMixin):

    account_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    email = models.EmailField(max_length=60, unique=True, blank=True, null=True)
    profile_pic = models.ImageField(null=True, blank=True,upload_to = "img/profile")
    contact_number = models.CharField(max_length=11, unique=True, validators=[
        RegexValidator(
            regex='(\+?0{1,9})[0-46-9][0-9]{7,9}$',
            message='Please use the correct contact number',
            code='invalid_contact_number'
        ),])

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False) #needed because want to access admin (to check permissions)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'dob', 'email']

    objects = UserManager()

    def __str__(self):
        return self.name