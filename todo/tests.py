from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Task

class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_task(self):
        url = reverse('todo:task-list')
        data = {'title': 'Test Task', 'description': 'Test Description', 'completed': False}
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')
        
        # Используем response.json() вместо response.data
        response_data = response.json()
        self.assertEqual(response_data['title'], 'Test Task')

    def test_get_tasks(self):
        Task.objects.create(title='Test Task', description='Test Description', completed=False)
        
        url = reverse('todo:task-list')
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Используем response.json() вместо response.data
        response_data = response.json()
        self.assertEqual(len(response_data), 1)
        self.assertEqual(response_data[0]['title'], 'Test Task')