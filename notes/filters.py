import django_filters
from .models import *

class NotesFilter(django_filters.FilterSet):

    class Meta:
        model = Note
        fields = {'title': ['icontains']}
