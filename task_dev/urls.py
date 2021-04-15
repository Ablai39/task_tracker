# django_auth/urls.py
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(('users.urls', 'users'), namespace='users')),
    path('', RedirectView.as_view(url='/user/', permanent=True)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)