from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from django.shortcuts import render

from django.core.cache import cache

from blog.models import Blog
from main_app.forms import ClientForm, MailingSetupForm, MailingMessageForm
from main_app.models import Client, MailingSetup, MailingMessage, Log


def home(request):
    blogs = Blog.objects.filter(is_published=True)
    mailings = MailingSetup.objects.all()
    mailings_is_published = MailingSetup.objects.filter(is_published=True)
    clients = Client.objects.values('email').distinct()

    context = {
        'blog_list': blogs.order_by('?')[:3],
        'mailings_list': mailings,
        'mailings_is_published': mailings_is_published,
        'clients_list': clients
    }

    return render(request, 'main_app/home.html', context)


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


class MailingSetupUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSetup
    form_class = MailingSetupForm
    success_url = reverse_lazy("main_app:mailing_list")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return super().get_form_class()
        raise PermissionDenied


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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingMessageForm
        raise PermissionDenied


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy("main_app:message_list")


class LogListView(ListView):
    model = Log
