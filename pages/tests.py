# SimpleTestCase is enough because homepage does not rely on the database
from django.test import SimpleTestCase
# import reverse to test URL and views
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location_homepageview(self):
        response = self.client.get("/")
        # homepage URL returns a 200 status code, no slug
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        response = self.client.get(reverse("home"))
        # homepage URL returns a 200 status code, slog 'home'
        self.assertEqual(response.status_code, 200)
        # use home.html
        self.assertTemplateUsed(response, "home.html")
        # contains “Home” in the response
        self.assertContains(response, "Home")