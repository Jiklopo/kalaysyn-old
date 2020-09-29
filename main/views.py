from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import *
from main.models import EventInfo, DayInfo


class IndexView(TemplateView):
    template_name = 'main.html'


class CalendarView(TemplateView):
    template_name = 'calendar.html'


class UserLoginView(LoginView):
    template_name = 'auth/login.html'


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('index')


class EventView(DetailView):
    template_name = 'events/detail.html'
    queryset = EventInfo.objects.all()


class EventCreateView(CreateView):
    form_class = EventForm
    template_name = 'events/form.html'


class EventUpdateView(UpdateView):
    form_class = EventForm
    template_name = 'events/form.html'
    queryset = EventInfo.objects.all()

    def get_success_url(self):
        return reverse('event-details', args=[self.object.id])


class EventDeleteView(DeleteView):
    template_name = 'events/confirm_delete.html'
    queryset = EventInfo.objects.all()
    success_url = reverse_lazy('calendar')


class DayInfoView(DetailView):
    template_name = 'day_info/detail.html'
    queryset = DayInfo.objects.all()


class DayInfoCreateView(CreateView):
    form_class = DayInfoForm
    template_name = 'day_info/form.html'


class DayInfoUpdateView(UpdateView):
    form_class = DayInfoForm
    template_name = 'day_info/form.html'
    queryset = DayInfo.objects.all()

    def get_success_url(self):
        return reverse('day-details', args=[self.object.id])


class DayInfoDeleteView(DeleteView):
    template_name = 'day_info/confirm_delete.html'
    queryset = DayInfo.objects.all()
    success_url = reverse_lazy('calendar')
