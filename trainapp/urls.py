from django.urls import path
from . import views
app_name = 'trainapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('booking/', views.trainappView, name='booking'),
    path('addbooking/',views.addbooking),
     


] 