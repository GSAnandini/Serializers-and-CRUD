from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('',home),
    path('add/',post_student),
    path('update/<int:id>/',update_student),
    path('delete/<int:id>/',delete_student),
]