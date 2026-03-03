from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.tasks.views import KanbanView
from kanban.admin_dashboard import admin_dashboard_view
from kanban.admin_dashboard import admin_dashboard_view, dashboard_stats_api


# Page d'accueil simple
def home(request):
    return HttpResponse("Project Manager API is running 🚀")


urlpatterns = [
    # 🔥 Dashboard custom AVANT admin
    path("admin/dashboard/", admin_dashboard_view, name="admin-dashboard"),
    path("admin/dashboard/stats/", dashboard_stats_api, name="admin-dashboard-stats"),

    # Admin Django
    path("admin/", admin.site.urls),

    # API JWT
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    # API Kanban
    path("api/kanban/", KanbanView.as_view(), name="kanban"),

    # Home
    path("", home),
]