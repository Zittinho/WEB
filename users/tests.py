from django.test import TestCase, Client
from django.contrib.auth.models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_login(self):
        login = self.client.login(username='testuser', password='12345')
        self.assertTrue(login)

    def test_session(self):
        self.client.login(username='testuser', password='12345')
        session = self.client.session
        session['key'] = 'value'
        session.save()
        self.assertEqual(self.client.session['key'], 'value')
