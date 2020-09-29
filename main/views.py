from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import *
from main.models import EventInfo, DayInfo


class IndexView(TemplateView):
    template_name = 'main.html'


class CalendarView(LoginRequiredMixin, TemplateView):
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = EventInfo.objects.filter(user=self.request.user)
        context['days'] = DayInfo.objects.filter(user=self.request.user)
        return context


class UserRegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('calendar')


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')


class UserLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True


class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'auth/password.html'
    success_url = reverse_lazy('calendar')


class EventView(LoginRequiredMixin, DetailView):
    template_name = 'events/detail.html'
    queryset = EventInfo.objects.all()


class EventCreateView(LoginRequiredMixin, CreateView):
    form_class = EventForm
    template_name = 'events/form.html'
    success_url = reverse_lazy('calendar')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.user = self.request.user
        event.save()
        return HttpResponseRedirect(self.success_url)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    form_class = EventForm
    template_name = 'events/form.html'
    queryset = EventInfo.objects.all()

    def get_success_url(self):
        return reverse('event-details', args=[self.object.id])


class EventDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'events/confirm_delete.html'
    queryset = EventInfo.objects.all()
    success_url = reverse_lazy('calendar')


class DayInfoView(LoginRequiredMixin, DetailView):
    template_name = 'day_info/detail.html'
    queryset = DayInfo.objects.all()


class DayInfoCreateView(LoginRequiredMixin, CreateView):
    form_class = DayInfoForm
    template_name = 'day_info/form.html'
    success_url = reverse_lazy('calendar')

    def form_valid(self, form):
        day = form.save(commit=False)
        day.user = self.request.user
        day.save()
        return HttpResponseRedirect(self.success_url)


class DayInfoUpdateView(LoginRequiredMixin, UpdateView):
    form_class = DayInfoForm
    template_name = 'day_info/form.html'
    queryset = DayInfo.objects.all()

    def get_success_url(self):
        return reverse('day-details', args=[self.object.id])


class DayInfoDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'day_info/confirm_delete.html'
    queryset = DayInfo.objects.all()
    success_url = reverse_lazy('calendar')
