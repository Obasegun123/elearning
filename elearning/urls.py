"""elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from courses import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('contact/', views.contact, name="contact"),
    path('accounts/', include('allauth.urls')),
    path('courses/', views.courses, name="courses"),
    path('courses/<int:course_id>/', views.course_detail, name="course_detail"),
    path('courses/english', views.English, name="english"),
    path('courses/math', views.Math, name="math"),
    path('courses/geography', views.Geography, name="geography"),
    path('courses/biology', views.Biology, name="biology"),
    path('courses/chemistry', views.Chemistry, name="chemistry"),
    path('tinymce/', include('tinymce.urls'))
    
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
