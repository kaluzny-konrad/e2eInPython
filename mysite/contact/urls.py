from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_view, name='contact_view'),
    path('thank-you/', views.thank_you_view, name='thank_you'),
]
