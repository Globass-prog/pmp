from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.http import JsonResponse
from django.db.models import Count
from django.db.models.functions import TruncMonth
from apps.tasks.models import Task
from apps.projects.models import Project


class CustomAdminSite(admin.AdminSite):
    site_header = "IT Project Manager Admin"
    site_title = "IT PM"
    index_title = "Dashboard"

    def get_urls(self):
        urls = super().get_urls()

        custom_urls = [
            path("dashboard/", self.admin_view(self.dashboard_view), name="dashboard"),
            path("dashboard/stats/", self.admin_view(self.dashboard_stats)),
        ]

        return custom_urls + urls

    def dashboard_view(self, request):
        return TemplateResponse(request, "admin/dashboard.html")

    def dashboard_stats(self, request):

        projects = Project.objects.count()
        tasks = Task.objects.count()
        done = Task.objects.filter(status="DONE").count()
        todo = Task.objects.filter(status="TODO").count()
        in_progress = Task.objects.filter(status="IN_PROGRESS").count()

        monthly = (
            Task.objects.filter(status="DONE")
            .annotate(month=TruncMonth("created_at"))
            .values("month")
            .annotate(total=Count("id"))
            .order_by("month")
        )

        labels = [m["month"].strftime("%b %Y") for m in monthly]
        performance = [m["total"] for m in monthly]

        return JsonResponse({
            "projects": projects,
            "tasks": tasks,
            "done": done,
            "todo": todo,
            "in_progress": in_progress,
            "performance_labels": labels,
            "performance_data": performance
        })


admin_site = CustomAdminSite(name="custom_admin")