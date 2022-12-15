from django.urls import path
from . import views
app_name = 'Dict'

urlpatterns = [
  path('', views.base, name='base')
]
