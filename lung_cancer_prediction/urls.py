from django.urls import path

from .views import index_form

urlpatterns = [
    path('', index_form, name='index_form'),
]
