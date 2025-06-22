from django.urls import path
from .views import TaskListCreateAPIView, TaskDetailAPIView

app_name = 'todo'  

urlpatterns = [
    path('tasks/', TaskListCreateAPIView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view(), name='task-detail'),
]