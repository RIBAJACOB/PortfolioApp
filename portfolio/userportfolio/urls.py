from django.conf.urls import  url
from .views import UserView, login_page, home_page


urlpatterns = [
    #path('', UserView.as_view(), name='home'),
    #path('/profile', )
    # url(r'^welcome/$',views.welcome.as_view(), name='welcome'), 
    url(r'^home/$',home_page,name='home'),
    url(r'^login/$',login_page,name='login'),
]