from django.urls import path
from . import views


urlpatterns = [
    path('Onlinestore/', views.landing_page, name='landing-page'),
]