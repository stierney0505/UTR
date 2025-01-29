"""
URL configuration for UnitTestRunner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from apps.errors import views

urlpatterns = [
    path('polls/', include('apps.polls.urls')),
    path('error/', include('apps.errors.urls')),
    path('admin/', admin.site.urls),
]

handler400 = 'apps.errors.views.error_views_4xx.custom_400'
handler403 = 'apps.errors.views.error_views_4xx.custom_403'
handler404 = 'apps.errors.views.error_views_4xx.custom_404'
handler500 = 'apps.errors.views.error_views_5xx.custom_500'
