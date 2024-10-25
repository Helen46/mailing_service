from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.forms import ClientForm, MailingSetupForm
from main_app.models import Client, MailingSetup


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
