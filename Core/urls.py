from django import urls
from django .urls import path
from .views import home

app_name='Core'

urlpatterns=[
    path('', home,name="home_view"),
]