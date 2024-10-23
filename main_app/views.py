from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main_app.forms import ClientForm
from main_app.models import Client


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
