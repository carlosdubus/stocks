from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/stocks', include('stocks.urls')),
] + static(settings.STATIC_URL)
