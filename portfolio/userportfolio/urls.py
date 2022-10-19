from django import views
from django.conf.urls import  url
from .views import UserView, login_page, home_page, details_page , view_details, logout_page


urlpatterns = [
    #path('', UserView.as_view(), name='home'),
    #path('/profile', )
    # url(r'^welcome/$',views.welcome.as_view(), name='welcome'), 
    url(r'^$',home_page,name='home'),
    url(r'^login/$',login_page,name='login'),
    url(r'^logout/$',logout_page,name='logout'),
    url(r'^view/$', view_details, name='view'),
    url(r'^details/$', details_page, name='details'),
]