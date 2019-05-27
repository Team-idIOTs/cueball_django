from django.urls import reverse, resolve
from django.test import TestCase
from .views import home, task_topic
from .models import Task

class HomeTests(TestCase):
    def setUp(self):
        self.task = Task.objects.create(name='dog', message='happy')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        task_topic_url = reverse('task_topic', kwargs={'pk': self.task.pk})
        self.assertContains(self.response, 'href="{0}"'.format(task_topic_url))
		

class TaskTopicsTests(TestCase):
    def setUp(self):
        Task.objects.create(name='dog', type='happy')

    def test_task_topic_view_success_status_code(self):
        url = reverse('task_topic', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_task_topic_view_not_found_status_code(self):
        url = reverse('task_topic', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_task_topic_url_resolves_task_topic_view(self):
        view = resolve('/tasks/1/')
        self.assertEquals(view.func, task_topic)

	def test_task_topic_view_contains_link_back_to_homepage(self):
		task_topic_url = reverse('task_topic', kwargs={'pk': 1})
		response = self.client.get(task_topic_url)
		homepage_url = reverse('home')
		self.assertContains(response, 'href="{0}"'.format(homepage_url))
		
