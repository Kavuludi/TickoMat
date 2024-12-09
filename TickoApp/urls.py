
from django.contrib import admin
from django.urls import path
from TickoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.base, name='base'),
    path('index/', views.index, name='index'),
    path('fleet/', views.fleet, name='fleet'),
    path('starter/', views.starter, name='starter'),
    path('routes/', views.routes, name='routes'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('contact/', views.contact, name='contact'),
    path('showcontact/', views.showcontact, name='contacts'),

    path('delete1/<int:id>', views.delete1, name='delete1'),

    path('edit1/<int:id>', views.edit1, name='edit1'),

    path('update1/<int:id>', views.update1, name='update1'),
    path('gallery/', views.gallery, name='gallery'),
    path('buses/', views.buses, name='buses'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('booking/', views.booking, name='booking'),
    path('trips/', views.trips, name='trips'),
    path('managetrips/', views.managetrips, name='managetrips'),
    path('showbooking/', views.mybookings, name='mybookings'),
    path('editbooking/<int:id>', views.editbooking, name='editbooking'),
    path('updatebooking/<int:id>', views.updatebooking, name='updatebooking'),
    path('delete/<int:id>', views.delete),

]
