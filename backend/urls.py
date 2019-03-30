from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/lead/', include('leads.urls')),
    path('', include('frontend.urls')),
]
