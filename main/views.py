from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView


class IndexView(TemplateView):
    template_name = 'main.html'


class CalendarView(TemplateView):
    pass


class CreateEventView(CreateView):
    pass

