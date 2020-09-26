from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.utils import timezone


def validate_rating_value(value):
    if value > 10 or value < 1:
        raise ValidationError(f'{value} must be in interval [1,10]!', params={'value': value})


class Emotions(models.TextChoices):
    FEAR = ('FR', 'Fear',)
    ANGER = ('AR', 'Anger')
    SADNESS = ('SD', 'Sadness')
    JOY = ('JY', 'Joy')
    DISGUST = ('DG', 'Disgust')
    SURPRISE = ('SP', 'Surprise')
    TRUST = ('TR', 'Trust')
    ANTICIPATION = ('AP', 'Anticipation')


class DayInfo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False, default=timezone.now)
    rating = models.IntegerField(validators=[validate_rating_value])
    emotions = ArrayField(models.CharField(max_length=30, choices=Emotions.choices), blank=True, null=True)
    description = models.TextField(max_length=300, blank=True, null=True)
    fatigue_rating = models.IntegerField(validators=[validate_rating_value], blank=True, null=True)
    sleep_rating = models.IntegerField(validators=[validate_rating_value], blank=True, null=True)
    productivity_rating = models.IntegerField(validators=[validate_rating_value], blank=True, null=True)
    things_done = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    appetite_rate = models.IntegerField(validators=[validate_rating_value], blank=True, null=True)
    meals_eaten = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    communication_rate = models.IntegerField(validators=[validate_rating_value], blank=True, null=True)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'date'], name='unique_user_date')]


class EventInfo(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    datetime = models.DateTimeField()
    rating = models.IntegerField(validators=[validate_rating_value])
    description = models.TextField(max_length=300, blank=True, null=True)
    emotions = ArrayField(models.CharField(max_length=30, choices=Emotions.choices), blank=True, null=True)
    is_hungry = models.BooleanField(blank=True, null=True)