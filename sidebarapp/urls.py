from django.conf.urls import url
from . import views

app_name="sidebar"

urlpatterns=[
    url(r"^$",views.IndexView,name="index"),
    url(r'^register/$',views.register,name="register"),
    url(r'^login/$',views.login_user,name="login"),
    url(r'^logout/$',views.logout_user,name="logout"),
    url(r'^rate/$',views.rate_movie,name="rate"),
]

"""url(r'^rate_movie/(?P<movie_id>[0-9]+)/$',views.rate_movie,name="rate"),"""
