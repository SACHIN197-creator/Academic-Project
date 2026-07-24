"""
URL configuration for bciitAcademicproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from testapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page, name = 'home'),
    path('students/', views.students_page, name='students'),

    path('faculty/', views.faculty_page, name='faculty'),

    path('events/', views.events_page, name='events'),
    path('enquiry/', views.enquiry_view, name='enquiry'),

    path('memb1/', views.anu_page, name='view1'),
    path('memb2/', views.sandeep_page, name='view2'),
    path('memb3/', views.sonia_page, name='view3'),
    path('memb4/', views.meetender_page, name='view4'),
    path('memb5/', views.shobha_page, name='view5'),
    path('memb6/', views.alok_page, name='view6'),
    path('memb7/', views.sanjna_page, name='view7'),
    path('memb8/', views.preeti_page, name='view8'),
    path('memb9/', views.pallavi_page, name='view9'),
    path('memb10/', views.harsh_page, name='view10'),
    path('memb11/', views.kritika_page, name='view11'),
    path('memb12/', views.lekhram_page, name='view12'),
    path('memb13/', views.monika_page, name='view13'),
    path('memb14/', views.palak_page, name='view14'),
    path('memb15/', views.keshav_page, name='view15'),
    path('memb16/', views.smriti_page, name='view16'),
]
