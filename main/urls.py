from django.conf.urls import url
from django.contrib import admin

from guests.views import Guests_Management, Guest_Confirm
from main.views import Test_View

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', Guest_Confirm.as_view(), name="guest_confirm"),
    url(r'^guests_management/$', Guests_Management.as_view(), name="guest_management"),
]
