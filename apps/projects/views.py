from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Project.objects.filter(members=self.request.user)

    def perform_create(self, serializer):
        project = serializer.save(owner=self.request.user)
        project.members.add(self.request.user)
        
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from django.db.models import Count
from apps.tasks.models import Task
from .models import Project


@staff_member_required
def admin_dashboard(request):
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()
    done_tasks = Task.objects.filter(status="DONE").count()

    completion_rate = 0
    if total_tasks > 0:
        completion_rate = round((done_tasks / total_tasks) * 100, 2)

    status_data = (
        Task.objects.values("status")
        .annotate(count=Count("id"))
        .order_by()
    )

    priority_data = (
        Task.objects.values("priority")
        .annotate(count=Count("id"))
        .order_by()
    )

    context = {
        "total_projects": total_projects,
        "total_tasks": total_tasks,
        "completion_rate": completion_rate,
        "status_data": list(status_data),
        "priority_data": list(priority_data),
    }

    return render(request, "admin/dashboard.html", context)