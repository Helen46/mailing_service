from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.forms import ClientForm, MailingSetupForm, MailingMessageForm
from main_app.models import Client, MailingSetup, MailingMessage


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("main_app:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("main_app:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy("main_app:client_list")


class MailingSetupListView(ListView):
    model = MailingSetup


class MailingSetupDetailView(DetailView):
    model = MailingSetup


class MailingSetupCreateView(CreateView):
    model = MailingSetup
    form_class = MailingSetupForm
    success_url = reverse_lazy("main_app:mailing_list")


class MailingSetupUpdateView(UpdateView):
    model = MailingSetup
    form_class = MailingSetupForm
    success_url = reverse_lazy("main_app:mailing_list")


class MailingSetupDeleteView(DeleteView):
    model = MailingSetup
    success_url = reverse_lazy("main_app:mailing_list")


class MailingMessageListView(ListView):
    model = MailingMessage


class MailingMessageDetailView(DetailView):
    model = MailingMessage


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy("main_app:message_list")


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy("main_app:message_list")


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy("main_app:message_list")
