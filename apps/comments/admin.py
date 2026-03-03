from django.contrib import admin
from django.db.models import Q
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ("task", "user", "created_at")
    list_filter = ("created_at",)
    search_fields = ("task__title", "user__username")

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Superuser voit tout
        if request.user.is_superuser:
            return qs

        # Sinon : commentaires liés aux projets où il est owner ou membre
        return qs.filter(
            Q(task__project__owner=request.user) |
            Q(task__project__members=request.user)
        ).distinct()