from . import views
from django.urls import path


urlpatterns = [
    path('contact/', views.contact_view, name='contact_view'),
]
