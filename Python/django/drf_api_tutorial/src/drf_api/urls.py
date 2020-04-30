
from django.contrib import admin
from django.urls import path, include
from core.views import TestView
from rest_framework.authtoken.views import ObtainAuthToken
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('', TestView.as_view(), name='test'),
    path('api/token', ObtainAuthToken, name='obtain-auth-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls'))
]
