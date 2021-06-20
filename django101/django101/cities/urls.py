# cities urls

from django.urls import path
from django.views.generic import TemplateView

from django101.cities.views import index, list_cities

urlpatterns = [
    path('', index),
    path('cities/', list_cities),
    # path('list/', TemplateView.as_view(template_name='cities.html')),

]

