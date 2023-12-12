from django.forms import ModelForm
from store.models import Product, User, Category, WorkDays
from django import forms
from django.conf import settings

MON = 'MONDAY'
TUE = 'TUESDAY'
WED = 'WEDNESDAY'
THU = 'THURSDAY'
FRI = 'FRIDAY'
SAT = 'SATURDAY'
SUN = 'SUNDAY'

# DAYS
DAYS_OF_WORK = [
    (MON, 'Monday'),
    (TUE, 'Tuesday '),
    (WED, 'Wednesday'),
    (THU, 'Thursday'),
    (FRI, 'Friday'),
    (SAT, 'Saturday'),
    (SUN, 'Sunday'),
]

class CreateEventForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput())
    creator = forms.CharField(widget=forms.TextInput(attrs={
        'readonly': True,
    }))
    print('creator:', User.username)
    category = forms.ModelChoiceField(queryset=Category.objects.all(),
                                       empty_label="Category is empty")
    description = forms.CharField(widget=forms.Textarea())
    price = forms.IntegerField(min_value=1, initial=100, required=True)
    number_of_guests = forms.IntegerField(initial=1, min_value=1, required=True)
    image = forms.ImageField(widget=forms.FileInput(), required=False)
    name_day = forms.CharField(widget=forms.TextInput())
    work_day = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=DAYS_OF_WORK,
    )
    beginning_of_work_day_time = forms.DateTimeField

    class Meta:
        model = Product
        fields = ('creator', 'name',
                  'description', 'price', 'image',
                  'number_of_guests',
                  'work_day')
