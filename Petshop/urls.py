from django.contrib import admin
from django.urls import path, include
from base.views import inicio, contato
from base.views import blog


urlpatterns = [
    path('', inicio),
    path('contato/', contato),
    path('reserva/', include('reserva.urls', namespace='reserva')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('rest_api.urls', namespace='api')),
    path('blog/', blog),
    
    
]
