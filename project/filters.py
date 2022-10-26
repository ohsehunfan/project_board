import django_filters
from project.models import OneTimeCode

class OneTimeCodeFilter(django_filters.Filter):
    class Meta:
        model = OneTimeCode
        fields = ['code']