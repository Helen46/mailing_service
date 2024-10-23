from django.urls import path

from main_app.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('main_app/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
]
