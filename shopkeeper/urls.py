from django.conf.urls import url
from shopkeeper import views

app_name = 'shopkeeper'

urlpatterns = [
    url(r'^$', views.shopkeeper_index_view),
    url(r'addproduct', views.addproduct_view, name="addproduct"),
    ]