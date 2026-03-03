from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required

# ✅ IMPORTS CORRECTS
from apps.projects.models import Project
from apps.tasks.models import Task
from django.http import JsonResponse

@staff_member_required
def admin_dashboard_view(request):
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()

    completed_tasks = Task.objects.filter(status="DONE").count()
    pending_tasks = Task.objects.filter(status="TODO").count()

    context = {
        "total_projects": total_projects,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
    }

    return render(request, "admin/dashboard.html", context)


def dashboard_stats_api(request):
    total_projects = Project.objects.count()
    total_tasks = Task.objects.count()
    done = Task.objects.filter(status="DONE").count()
    todo = Task.objects.filter(status="TODO").count()
    in_progress = Task.objects.filter(status="IN_PROGRESS").count()

    return JsonResponse({
        "projects": total_projects,
        "tasks": total_tasks,
        "done": done,
        "todo": todo,
        "in_progress": in_progress,
    })