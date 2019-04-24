from django.conf.urls import url
from buyer import views

app_name = 'buyer'

urlpatterns = [

    url(r'^$', views.home_view, name="home"),
    url(r'^login/$', views.login_view, name="login"),
    url(r'^signup/$', views.signup_view, name="signup"),
    url(r'buyerdashboard',views.buyredashboard_view,name="buyerdashboard"),

]
