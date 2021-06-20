from django.contrib import admin
from django.urls import path, include

from django101.cities.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('django101.cities.urls')),
    path('people', include('django101.people.urls')),
]
