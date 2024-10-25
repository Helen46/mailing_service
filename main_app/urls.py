from django.urls import path

from main_app.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, \
    MailingSetupListView, MailingSetupDetailView, MailingSetupUpdateView, MailingSetupCreateView, MailingSetupDeleteView

urlpatterns = [
    path('', ClientListView.as_view(), name='client_list'),
    path('main_app/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('create/', ClientCreateView.as_view(), name='client_create'),
    path('update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),
    path('mailing/', MailingSetupListView.as_view(), name='mailing_list'),
    path('mailing/<int:pk>', MailingSetupDetailView.as_view(), name='mailing_detail'),
    path('mailing/create/', MailingSetupCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>', MailingSetupUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete/<int:pk>', MailingSetupDeleteView.as_view(), name='mailing_delete'),
]
