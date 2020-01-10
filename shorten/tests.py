from django.test import TestCase
from .models import Link
from django.shortcuts import reverse
import random, string

class ShortenTest(TestCase):
    def setUp(self):
        """
        Setup method to create relevant data for the tests
        """
        self.url = "http://www.example.com/"
        self.l = Link(url=self.url)
        self.short_url = Link.shorten(self.l)
        
    def test_shortens(self):
        """
        Test that urls get shorter
        """
        self.assertLess(len(self.short_url), len(self.url))

    def test_recover_link(self):
        """
        Tests that shortened and expanded url is the same as original
        """
        self.l.save()
        # Another user asks for the expansion of short_url
        exp_url = Link.expand(self.short_url)
        self.assertEqual(self.url, exp_url)

    def test_homepage(self):
        """
        Tests that a home page exists and it contains a form.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("form", response.context)

    def test_redirect_to_long_link(self):
        """
        Tests that submitting the forms returns a Link object.
        """
        response = self.client.get(
            reverse("redirect_short_url",
                    kwargs={"short_url": self.short_url}))
        self.assertRedirects(response, self.url, status_code=302)
