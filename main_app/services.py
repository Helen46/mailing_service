from datetime import timedelta

from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from main_app.models import MailingSetup, Log


def send_mailing(email, topic, body):
    """Отправка письма"""
    return send_mail(subject=topic, message=body, recipient_list=[email], from_email=settings.EMAIL_HOST_USER, fail_silently=True)


def set_next_send():
    """Дата следующей рассылки"""
    ms = MailingSetup.objects.filter(next_send__isnull=True)
    for m in ms:
        m.next_send = m.start
        m.save()


def send_mailings():
    """Рассылка"""
    set_next_send()
    now = timezone.now()
    ms = MailingSetup.objects.filter(next_send__date=now.date())
    for m in ms:
        for client in m.clients.all():
            if send_mailing(client.email, m.message.topic, m.message.body):
                Log.objects.create(status="success", mailing=m, client=client)
            else:
                Log.objects.create(status="unsuccess", mailing=m, client=client)

        if m.periodicity == "daily":
            m.next_send += timedelta(days=1)
        elif m.periodicity == "weekly":
            m.next_send += timedelta(days=7)
        elif m.periodicity == "monthly":
            m.next_send += timedelta(days=30)

        m.save()
