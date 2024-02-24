from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage, name = 'homepage'),
    path('portfolio/', views.portpage, name = 'portpage'),
    path('services/', views.servicepage, name = 'servicepage'),
    path('blogdetails/', views.blogdetailpage, name = 'blogdetailpage'),
    path('blog/', views.blogpage, name = 'blogpage')


]