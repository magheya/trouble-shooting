from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('expert-system/', views.expert_system_view, name='expert_system_view'),
    path('',include('api.urls'))
]

