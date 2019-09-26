from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True,
    )
    member_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=10, verbose_name='Nome')
    last_name = models.CharField(max_length=50, verbose_name='Sobrenome')
    leader = models.CharField(max_length=50, verbose_name='Lider', default=None)
    department = models.CharField(max_length=30, verbose_name='Area', default=None)
    post = models.CharField(max_length=30, verbose_name='Cargo')

