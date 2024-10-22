from django.urls import path

from main_app.views import ClientListView, ClientDetailView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('main_app/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
]
