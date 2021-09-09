from django.conf.urls import url
from . import views



urlpatterns = [
    url('calendar/', views.CalendarView.as_view(), name='Calendar'),
    url('forms/', views.event, name='event_form'), 
 

]