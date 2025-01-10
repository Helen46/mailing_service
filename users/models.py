from django.contrib.auth.models import AbstractUser
from django.db import models

from config.settings import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="email",
        help_text="Введите вашу электронную почту"
    )
    first_name = models.CharField(
        max_length=35,
        verbose_name="Имя",
        help_text="Введите вашу имя",
        **NULLABLE
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
        **NULLABLE
    )
    phone = models.CharField(
        max_length=35,
        verbose_name="Телефон",
        **NULLABLE,
        help_text="Введите ваш номер телефона"
    )
    country = models.CharField(
        max_length=150,
        verbose_name="Страна",
        **NULLABLE,
        help_text="Введите название вашей сраны"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        verbose_name="Аватар",
        **NULLABLE,
        help_text="Загрузите фото"
    )
    token = models.CharField(
        max_length=100,
        verbose_name="Token",
        **NULLABLE
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Metta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
