from django.urls import path

from main.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('calendar', CalendarView.as_view(), name='calendar'),

    path('login', UserLoginView.as_view(), name='login'),
    path('logout', UserLogoutView.as_view(), name='logout'),

    path('events/<int:pk>', EventView.as_view(), name='event-details'),
    path('events/new', EventCreateView.as_view(), name='event-new'),
    path('events/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),

    path('day_info/new', DayInfoCreateView.as_view(), name='day-new'),
    path('day_info/<int:pk>', DayInfoView.as_view(), name='day-details'),
    path('day_info/<int:pk>/update', DayInfoUpdateView.as_view(), name='day-update'),
    path('day_info/<int:pk>/delete', DayInfoDeleteView.as_view(), name='day-delete')
]
