from django.urls import path
from FirstApp import views
from django.conf import settings 
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name='home'),
    path('second/',views.second,name='second'),
    path('third/',views.Time,name='time'),
    path('flex/',views.Student,name='flex'),
    path('student_record/',views.Student_Record,name='student_record'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('register/',views.register,name='register'),
    path('id_profile/',views.id_profile,name='id_profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)