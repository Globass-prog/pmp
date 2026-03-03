from django.contrib import admin
from django.db.models import Q
from .models import Task

from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'project',
        'status',
        'priority',
        'assigned_to',
        'due_date',
        'created_at'
    )

    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    list_editable = ('status', 'priority')
    ordering = ('-created_at',)

    def is_overdue(self, obj):
        from django.utils.timezone import now
        if obj.due_date and obj.due_date < now().date():
            return "⚠ Overdue"
        return "OK"
    is_overdue.short_description = "Deadline"

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(
            Q(project__owner=request.user) |
            Q(project__members=request.user)
        ).distinct()