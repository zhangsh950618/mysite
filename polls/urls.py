from . import views
from django.conf.urls import url


urlpatterns = [url(r'^$', views.IndexView.as_view(), name='index'),
               # ex:/polls/5/
               # ?P<question> define the name identify the matched pattern
               # [0-9]+ is a regular experssion to match a squence of digits
               url(r'^(?P<pk>[0-9]+)/$',
                   views.DetailView.as_view(), name='detail'),
               url(r'^(?P<pk>[0-9]+)/result/$',
                   views.ResultView.as_view(), name='result'),
               url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
               ]
