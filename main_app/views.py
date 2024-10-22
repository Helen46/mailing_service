from django.views.generic import ListView, DetailView

from main_app.models import Client


class ClientListView(ListView):
    model = Client


class ClientDetailView(DetailView):
    model = Client
