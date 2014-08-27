from django.conf.urls import patterns, url

from pages import views

urlpatterns = patterns('',
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r"^$", views.DetailView.as_view(), kwargs={'slug': "home"}),
    url(
        r'^(?P<slug>[-_a-z0-9]+)/$',
        views.DetailView.as_view(), name="detail"
        ),
    )
