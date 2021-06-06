from django.test import TestCase
from django.shortcuts import reverse
from ..models import Profile, Service, Project, Client, Contact
from django.utils import timezone


class IndexViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:index'))
        self.assertEqual(response.status_code, 200)


class AboutViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Profile.objects.create(
            name='name',
            description='description',
            b_date=timezone.now(),
            occupation='occupation',
            email='email@mail.com',
            phone='99999999999',
        )

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:about'))
        self.assertEqual(response.status_code, 200)

    """
    def test_profile_on_context(self):
        profile = Profile.objects.get(pk=1)
        response = self.client.get(reverse('portfolio:about'))
        self.assertEqual(
            response.context['profile'],
            profile,
        )
    """


class ServicesViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        Service.objects.create(name='name', description='description')

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:service'))
        self.assertEqual(response.status_code, 200)

    def test_one_service(self):
        response = self.client.get(reverse('portfolio:service'))
        self.assertQuerysetEqual(response.context['service_list'], ['<Service: name>'])

    def test_many_services(self):
        Service.objects.create(name='name', description='description')
        response = self.client.get(reverse('portfolio:service'))
        self.assertQuerysetEqual(
            response.context['service_list'],
            ['<Service: name>', '<Service: name>'],
            ordered=False
        )


class PortfolioViewTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        service = Service.objects.create(name='name', description='description')
        client = Client.objects.create(name='name', email='email@mail.com', phone='99999999999', city='city')
        for i in range(7):
            Project.objects.create(
                name='name',
                description='description',
                service=service,
                client=client,
                date=timezone.now(),
            )

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:portfolio'))
        self.assertEqual(response.status_code, 200)

    def test_lasted_six_project(self):

        url = reverse('portfolio:portfolio')
        response = self.client.get(url)
        self.assertQuerysetEqual(
            response.context['project_list'],
            ['<Project: name>', '<Project: name>', '<Project: name>',
             '<Project: name>', '<Project: name>', '<Project: name>'],
        )


class ContactViewTests(TestCase):

    def test_status_200(self):
        response = self.client.get(reverse('portfolio:contact'))
        self.assertEqual(response.status_code, 200)

    # def test_redirect_success_url(self):

