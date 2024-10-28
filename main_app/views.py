from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main_app.forms import ClientForm, MailingSetupForm, MailingMessageForm
from main_app.models import Client, MailingSetup, MailingMessage, Log


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client


class ClientCreateView(CreateView, LoginRequiredMixin):
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy("main_app:client_list")

    def form_valid(self, form):
        client = form.save()
        user = self.request.user
        client.owner = user
        client.save()

        return super().form_valid(form)


class ClientUpdateView(UpdateView, LoginRequiredMixin):
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


class MailingSetupCreateView(CreateView, LoginRequiredMixin):
    model = MailingSetup
    form_class = MailingSetupForm
    success_url = reverse_lazy("main_app:mailing_list")

    def form_valid(self, form):
        mailing = form.save()
        user = self.request.user
        mailing.owner = user
        mailing.save()

        return super().form_valid(form)


class MailingSetupUpdateView(UpdateView, LoginRequiredMixin):
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


class MailingMessageCreateView(CreateView, LoginRequiredMixin):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy("main_app:message_list")

    def form_valid(self, form):
        message = form.save()
        user = self.request.user
        message.owner = user
        message.save()

        return super().form_valid(form)


class MailingMessageUpdateView(UpdateView, LoginRequiredMixin):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy("main_app:message_list")


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy("main_app:message_list")


class LogListView(ListView):
    model = Log
