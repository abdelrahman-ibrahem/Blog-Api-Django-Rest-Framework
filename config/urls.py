from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/' , include('blog.urls')),
    path('api-auth/' , include('rest_framework.urls')),
    path('api-auth/dj-rest-auth/' , include('dj_rest_auth.urls')),
    path('api-auth/dj-rest-auth/registration' , include('dj_rest_auth.registration.urls')),
]
