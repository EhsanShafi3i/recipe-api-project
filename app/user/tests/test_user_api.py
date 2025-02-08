"""Test for the user API."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

CREATE_USER_URL = reverse("user:create")


def create_user(**params):
    """Create and return a new user."""
    return get_user_model.objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the public features of the user API."""

    def setUp(self):
        """Set up the client."""
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successful."""
        payload = {
            "email": "test@example",
            "password": "testpass1234",
            "name": "test name",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_with_email_exists_error(self):
        """Test error returned if user with email exists."""
        payload = {
            "email": "test@example",
            "password": "testpass1234",
            "name": "test name",
        }
        create_user(payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_for_short_password_error(self):
        """Test if error happens if its shorter than cretin amount."""
        payload = {"email": "test@example", "password": "test", "name": "test name"}
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        existence = get_user_model().objects.filter(email=payload["email"]).exists()
        self.assertFalse(existence)
