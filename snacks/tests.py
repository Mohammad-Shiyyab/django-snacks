from django.test import SimpleTestCase
from django.urls import reverse


class TestHome(SimpleTestCase):
    def test_status_code(self):
        url = reverse('home')
        response = self.clinet.get(url)
        self.assertEqual(response.statuse_code, 200)


    def test_home_page_template(self):
        url = reverse('home')
        response = self.clinet.get(url)
        self.assertTemplateUsed(response, 'home.html')


