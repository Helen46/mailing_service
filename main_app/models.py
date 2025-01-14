from django.db import models

from config.settings import NULLABLE
from users.models import User


class Client(models.Model):
    first_name = models.CharField(
       max_length=50,
       verbose_name="Имя клиента",
       help_text="Введите имя",
    )
    midl_name = models.CharField(
        max_length=50,
        verbose_name="Отчество клиента",
        help_text="Введите отчество",
        **NULLABLE,
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия клиента",
        help_text="Введите фамилию",
    )
    email = models.EmailField(
        max_length=150,
        verbose_name="Email клиента",
        help_text="Введите контактный email",
    )
    comment = models.TextField(
        verbose_name="Коментарий",
        help_text="Введите коментарий",
        ** NULLABLE,
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.SET_NULL,
        **NULLABLE
    )

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ('last_name',)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class MailingSetup(models.Model):
    PERIODS = (
        ("once", 'Единоразовая'),
        ("daily", 'Ежедневная'),
        ("weekly", 'Раз в неделю'),
        ("monthly", 'Раз в месяц'),
    )
    STATUSES = (
        ("created", 'Создана'),
        ("started", 'Запущена'),
        ("finished", 'Завершена'),
    )
    start = models.DateTimeField(
        verbose_name="Дата начала первой рассылки",
    )
    next_send = models.DateTimeField(
        **NULLABLE,
        verbose_name="Дата следующей отправки",
    )
    periodicity = models.CharField(
        verbose_name="Переодичность рассылки",
        choices=PERIODS,
        default="once",
    )
    status = models.CharField(
        verbose_name="Статус рассылки",
        choices=STATUSES,
        default="created",
    )
    clients = models.ManyToManyField(
        Client,
        related_name="Clients",
    )
    message = models.ForeignKey(
        "MailingMessage",
        related_name="messages",
        on_delete=models.SET_NULL,
        verbose_name="Сообщение рассылки",
        null=True
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.SET_NULL,
        **NULLABLE
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name="Опубликовано",
        help_text="Отметьте для активации"
    )

    class Meta:
        verbose_name = "Настройка рассылки"
        verbose_name_plural = "Настройки рассылок"
        ordering = ('start',)
        permissions = [
            ("block_user", "Can block user"),
            ("disable_mailings", "Can disable mailings"),
        ]

    def __str__(self):
        return f'Рассылка {self.periodicity}. Дата начала: {self.start}. Статус: {self.status}'


class MailingMessage(models.Model):
    topic = models.CharField(
        max_length=300,
        verbose_name="Тема рассылки",
        help_text="Введите тему рассылки",
    )
    body = models.TextField(
        verbose_name="Содержание рассылки",
    )
    owner = models.ForeignKey(
        User,
        verbose_name='Владелец',
        on_delete=models.SET_NULL,
        **NULLABLE
    )

    class Meta:
        verbose_name = "Сообщение рассылки"
        verbose_name_plural = "Сообщения рассылок"
        ordering = ('topic',)

    def __str__(self):
        return f'{self.topic}'


class Log(models.Model):
    STATUS_LOG = (
        ("success", "успешно"),
        ("unsuccess", "неуспешно")
    )

    time = models.DateTimeField(
        verbose_name="Дата и время попытки отправки", auto_now_add=True
    )
    status = models.CharField(
        max_length=50,
        choices=STATUS_LOG,
        verbose_name='Cтатус рассылки'
    )
    server_response = models.CharField(
        max_length=150,
        verbose_name="Ответ сервера почтового сервиса",
        **NULLABLE
    )
    mailing = models.ForeignKey(
        MailingSetup,
        on_delete=models.CASCADE,
        verbose_name="Рассылка"
    )
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        verbose_name="клиент",
        **NULLABLE
    )

    def __str__(self):
        return f"{self.mailing} {self.time} {self.status} {self.server_response}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылок"
