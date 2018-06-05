from django import forms
from django.contrib.auth.models import User
from cms.models import Kind, Food, Device
import django_filters


class UserFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(label='ユーザー名', lookup_expr='contains')
    first_name = django_filters.CharFilter(label='名', lookup_expr='contains')
    last_name = django_filters.CharFilter(label='姓', lookup_expr='contains')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', ]


class FoodFilter(django_filters.FilterSet):
    kind = django_filters.ModelMultipleChoiceFilter(queryset=Kind.objects.all(),
        widget=forms.CheckboxSelectMultiple)
    #   django_filters.ChoiceFilter(choices=STATUS_CHOICES)
    name = django_filters.CharFilter(label='名前', lookup_expr='contains')

    class Meta:
        model = Food
        fields = ['kind', 'name', ]


class IndexFilter(django_filters.FilterSet):
    deviceid = django_filters.CharFilter(label='デバイスID', )   # lookup_expr='contains', )
    time = django_filters.CharFilter()

    class Meta:
        model = Device
        fields = ['deviceid', ]
