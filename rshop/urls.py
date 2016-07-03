from django.conf.urls import url
from django.contrib import admin
import personal.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signin/', personal.views.signin, name='signin'),
    url(r'^signup/', personal.views.signup, name='signup'),
    url(r'^profile/', personal.views.profile, name='profile'),
    url(r'^signout/', personal.views.signup, name='signout'),
]
