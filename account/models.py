import re

from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin,
                                        UserManager)
from django.conf import settings


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        'Nome de Usuário', max_length=30, unique=True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),
                                              'O nome de usuário só pode conter letras, digitos ou os '
                                              'seguintes caracteres: @/./+/-/_', 'invalid')]
    )
    email = models.EmailField('E-mail', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    cpf = models.CharField('CPF', max_length=15)
    birth_data = models.DateField('Data de nascimento', blank=True)
    contact_phone = models.CharField('Telefone de contato', max_length=15, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username

    def get_short_name(self):
        return self.username

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'


class PasswordReset(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Usuário', related_name='requests_password_reset',
                             on_delete=models.CASCADE)
    key = models.CharField('Chave de reset', max_length=100, unique=True)
    creation_date = models.DateTimeField('Data de criação', auto_now_add=True)
    confirmed = models.BooleanField('Confirmação de recebimento', default=False, blank=True)

    def __str__(self):
        return '{0} em {1}'.format(self.user, self.creation_date)

    class Meta:


        verbose_name = 'Solicitação de nova senha'
        verbose_name_plural = 'Solicitações de novas senhas'
        ordering = ['-creation_date']
