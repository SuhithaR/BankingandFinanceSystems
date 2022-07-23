from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from accounts import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^accounts/', include("accounts.urls")),
    url(r'^profiles/', include("profiles.urls"))
]


