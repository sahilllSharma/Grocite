from django.urls import path
from . import views
app_name = 'myapp1'
urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('detail/<int:type_no>', views.detail, name='detail'),
 path('test',views.test,name='test'),
 path('items/', views.items, name='items'),
 path('items/<int:item_id>', views.itemdetail, name='itemdetail'),
 path('placeorder/', views.placeorder, name='placeorder'),

]