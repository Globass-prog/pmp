from django.contrib import admin
from django.db.models import Q
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "owner",
        "members_count",
        "tasks_count",
        "created_at",
    )

    list_filter = ("created_at",)
    search_fields = ("name", "owner__username")
    filter_horizontal = ("members",)
    ordering = ("-created_at",)

    def members_count(self, obj):
        return obj.members.count()
    members_count.short_description = "Members"

    def tasks_count(self, obj):
        return obj.tasks.count()  # ✅ ici
    tasks_count.short_description = "Tasks"

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        if request.user.is_superuser:
            return qs

        return qs.filter(
            Q(owner=request.user) |
            Q(members=request.user)
        ).distinct()