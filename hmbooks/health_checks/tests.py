from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse


class HealthCheckTestCase(TestCase):
    def setUp(self):
        """Define the test client"""
        self.client = APIClient()
        # self.response = self.client.get(reverse('health:health'))
        self.response = self.client.get("/health/")

    def test_api_returns_OK_payload(self):
        # check not empty payload
        self.assertIsNotNone(self.response)
        # check content
        # self.assertContains(self.response,"OK")
        self.assertEqual(self.response.data["api"], "OK")

    def test_api_returns_status_code_200(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)