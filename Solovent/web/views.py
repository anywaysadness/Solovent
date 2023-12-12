from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from store.models import Product,WorkDays
from web.forms import CreateEventForm

from common.views import TitleMixin


# Home page
class IndexView(TitleMixin, TemplateView):
    template_name = 'web/index.html'
    title = 'Solovent - Home'


# Class for create new events
class CreateEventView(TitleMixin, SuccessMessageMixin, CreateView):
    model = WorkDays
    form_class = CreateEventForm
    template_name = 'web/create_event.html'
    success_url = reverse_lazy('store:catalog')
    success_message = 'You have successfully create!'
    title = 'Solovent - Create event'

    def get_queryset(self):
        queryset = super(CreateEventView, self).get_queryset()
