from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate_prompt, name='generate_prompt'),
    path('generate-prompt/', views.ajax_generate_prompt, name='ajax_generate_prompt'),
]