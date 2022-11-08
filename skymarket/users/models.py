from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    USER = "user"
    ADMIN = "admin"
    ROLES = [(USER, "пользователь"), (ADMIN, "администратор")]


class User(AbstractBaseUser):
    first_name = models.CharField(max_length=15, verbose_name=_("Имя"))
    last_name = models.CharField(max_length=15, verbose_name=_("Фамилия"))
    phone = PhoneNumberField(max_length=12, verbose_name=_("Телефон"))
    email = models.EmailField(unique=True, verbose_name=_("Почта"))
    role = models.CharField(max_length=5, choices=UserRoles.ROLES, default=UserRoles.USER, verbose_name=_("Роль"))
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to="user_picture/", null=True, blank=True, verbose_name=_("Аватарка"))

    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone', "role"]

    @property
    def is_admin(self):
        return self.role == UserRoles.ADMIN

    @property
    def is_user(self):
        return self.role == UserRoles.USER

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()
