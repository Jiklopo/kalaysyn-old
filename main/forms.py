from django.forms import ModelForm

from main import models


class EventForm(ModelForm):
    class Meta:
        model = models.EventInfo
        fields = ['datetime', 'name', 'rating', 'description', 'emotions', 'is_hungry']


class DayInfoForm(ModelForm):
    class Meta:
        model = models.DayInfo
        fields = ['date', 'rating', 'emotions', 'description', 'fatigue_rating', 'sleep_rating', 'productivity_rating',
                  'things_done', 'appetite_rate', 'meals_eaten', 'communication_rate']
