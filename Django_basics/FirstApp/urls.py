from django.urls import path
from FirstApp import views
urlpatterns = [
    path('',views.index,name='home'),
    path('second/',views.second,name='second'),
    path('third/',views.Time,name='time')
]