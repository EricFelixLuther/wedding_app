from django.conf.urls import url
from django.contrib import admin

from guests.views import Guests_Management
from main.views import Test_View

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Test_View.as_view(), name="test"),
    url(r'^guests_management/', Guests_Management.as_view(), name="guest_management"),
]
