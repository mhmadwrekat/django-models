from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class SnacksTests(TestCase) :
    def test_home_page_status_code(self) :
        url = reverse('snack_list')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_home_page_template(self) :
        url = reverse('snack_list')
        resp = self.client.get(url)
        self.assertTemplateUsed(resp, "snack_list.html")
        self.assertTemplateUsed(resp, "_base.html")
