from django.urls import path
from project_manager.admin import admin_site

urlpatterns = [
    path('admin/', admin_site.urls),
]