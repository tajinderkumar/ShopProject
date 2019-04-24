from django.conf.urls import url
from manager import views

app_name = 'manager'

urlpatterns = [
    url(r'^$', views.manager_view),
    url(r'changepassword', views.change_password_view, name= "changepassword"),
    url(r'producttype', views.producttype_view, name="producttype"),
    url(r'category', views.productcategory_view, name="category"),
    url(r'brand', views.productbrand_view, name="brand"),
    url(r'size',views.productsize_view, name="size")
    ]