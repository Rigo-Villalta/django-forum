from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    is_moderator = models.BooleanField(_("moderator"), default=False)
    age = models.IntegerField(verbose_name=_("edad"), blank=False, null=False)
