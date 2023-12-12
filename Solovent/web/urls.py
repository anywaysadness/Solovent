from django.urls import path
from web.views import CreateEventView
from django.contrib.auth.decorators import login_required


app_name = 'web'

urlpatterns = [
    # create new product
    path('create_event/', CreateEventView.as_view(), name='create_event'),
]
