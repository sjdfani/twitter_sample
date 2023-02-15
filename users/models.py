from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager


class User(AbstractUser):
    first_name = None
    last_name = None
    username = models.CharField(_('Username'), max_length=20)
    email = models.EmailField(_("Email address"), unique=True)
    fullname = models.CharField(
        _('Fullname'), max_length=50, null=True, blank=True)
    bio = models.TextField(_('Bio'), null=True, blank=True)
    locations = models.CharField(
        _('Locations'), max_length=50, null=True, blank=True)
    website = models.CharField(
        _('Website'), max_length=100, null=True, blank=True)
    birthdate = models.DateField(_('Birthdate'), null=True, blank=True)
    cover_photo = models.ImageField(_('Cover photo'), null=True, blank=True)
    profile_photo = models.ImageField(
        _('Profile photo'), null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username',]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
