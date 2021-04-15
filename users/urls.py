from django.conf.urls import url
from .views import CreateUserAPIView, UserRetrieveUpdateAPIView
from users import views
 
urlpatterns = [
    url(r'^index$', views.index),
    url(r'^$', views.index),
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^obtain_token/$', views.authenticate_user),
]