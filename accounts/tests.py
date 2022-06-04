# contains Django's signup form 
from django.contrib.auth import get_user_model
# to run tests that touch the database
from django.test import TestCase
# to verify the URL and view work properly
from django.urls import reverse


class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self):
        # is the sign up page at the correct URL ...
        response = self.client.get("/accounts/signup/")
        # ... and returns a 200 status code
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self):
        # checks the view, reverses signup which is the URL name
        response = self.client.get(reverse("signup"))
        # returns a 200 status code
        self.assertEqual(response.status_code, 200)
        # signup.html template is being used
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self):
        # checks the form by sending a post request to fill it out with ...
        # ... user data
        response = self.client.post(
            reverse("signup"),
            {
                "username": "testuser",
                "email": "testuser@email.com",
                "password1": "testpass123",
                "password2": "testpass123",
            },
        )
        # expect a 302 redirect after the form is submitted
        self.assertEqual(response.status_code, 302)
        # confirm that there is now one user in the test database ...
        self.assertEqual(get_user_model().objects.all().count(), 1)
        # ... with a matching username and ...
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        # ... email address
        self.assertEqual(get_user_model().objects.all()[0].email, "testuser@email.com")