"""mytaxi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

import apps.client.views

schema_view = get_schema_view(
   openapi.Info(
      title="MyTaxi loyihasi uchun API",
      default_version='v1',
      description="MyTaxi loyihasi uchun API dokumentatsiyasi",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="asilbekmirolimov@gmail.com"),
      license=openapi.License(name="MyTaxi License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('login/', apps.client.views.LoginPage, name='login-page'),
    path('', apps.client.views.HomePage, name='home-page'),
    path('about/', apps.client.views.About, name='about-page'),
    path('news/', apps.client.views.News, name='news-page'),
    path('contact/', apps.client.views.ContactUs, name='contact-page'),

    path('api/v1/client/', include("apps.client.urls")),
    path('api/v1/driver/', include("apps.driver.urls")),
    path('api/v1/order/', include("apps.order.urls")),

    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
