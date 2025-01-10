from django.forms import BooleanField, ModelForm
from django import forms

from main_app.models import Client, MailingSetup, MailingMessage


class StileFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ClientForm(StileFormMixin, ModelForm):
    class Meta:
        model = Client
        exclude = ("owner",)


class MailingSetupForm(StileFormMixin, ModelForm):
    class Meta:
        model = MailingSetup
        exclude = ('owner',)
        widgets = {
            "start": forms.DateInput(
                format="%Y-%m-%d %H:%M:%S",
                attrs={
                    "class": "form-control",
                    "placeholder": "Select a date",
                    "type": "datetime-local",
                },
            ),
        }


class MailingMessageForm(StileFormMixin, ModelForm):
    class Meta:
        model = MailingMessage
        exclude = ("owner",)
