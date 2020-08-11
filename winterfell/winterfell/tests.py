from django.test import TestCase
from rest_framework import status


class WinterfellViewTest(TestCase):

    def test_drycleaning_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, "drycleaning.html")
