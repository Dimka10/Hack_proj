from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.mail import send_mail

from hack_proj.settings import EMAIL_HOST_USER


class UserManager(BaseUserManager):
    use_in_migrations = True

    def email_user(self, email, password, *args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password, *args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user

    def create_superuser(self, email, password, *args, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, *args, **kwargs)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class ContactMethod(models.TextChoices):
    whatsapp = ('whatsapp', 'Whatsapp')
    telephone = ('telephone', 'Phone Number')
    mail = ('mail', 'Mail')


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        return self.is_staff

    def create_activation_code(self):
        from django.utils.crypto import get_random_string
        code = get_random_string(6, '123456789')
        self.activation_code = code
        self.save()

    def send_activation_email(self):
        msg = f"""
            Thank you for your registration!
            Your activation code is: http://localhost:8000/auth/account/activate/{self.activaton_code}/
        """
        send_mail('Account activation',
                  msg,
                  EMAIL_HOST_USER,
                  [self.email, ]
                  )

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
