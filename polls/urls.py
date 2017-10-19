from django.conf.urls import url
from . import views

# Create your views here.

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add/$', views.InsertView.as_view(), name='mapimage-add'),
]
    
