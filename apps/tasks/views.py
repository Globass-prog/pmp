from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = Task.objects.all()

    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(project__members=self.request.user)
    



class KanbanView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        project_id = request.query_params.get("project_id")

        if not project_id:
            return Response({"error": "project_id is required"}, status=400)

        tasks = Task.objects.filter(project_id=project_id)

        data = {}

        for status, _ in Task.STATUS_CHOICES:
            filtered = tasks.filter(status=status)
            data[status] = TaskSerializer(filtered, many=True).data

        return Response(data)