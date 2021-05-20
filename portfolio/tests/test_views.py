from django.test import TestCase
from django.shortcuts import reverse


class IndexViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)


class AboutViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:about'))
        self.assertEqual(response.status_code, 200)


class ServicesViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:services'))
        self.assertEqual(response.status_code, 200)


class PortfolioViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:portfolio'))
        self.assertEqual(response.status_code, 200)


class ContactViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)


