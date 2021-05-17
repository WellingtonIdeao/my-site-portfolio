from django.test import TestCase
from ..models import Contact, Client, Profile, Service, Project, ImageProject
from django.utils import timezone


class ContactModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Contact.objects.create(name='name', email='mail@mail.com', subject='subject', message='message')

    """ def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        Contact.objects.create(name='name', email='mail@mail.com', subject='subject', message='message')
    """

    def test_name_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def test_subject_max_length(self):
        contact = Contact.objects.get(id=1)
        max_length = contact._meta.get_field('subject').max_length
        self.assertEqual(max_length, 50)


class ClientModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        Client.objects.create(name='name', email='mail@mail.com', phone='99999999999', city='City-State')

    def test_name_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('name').max_length
        self.assertEqual(max_length, 50)

    def test_email_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('email').max_length
        self.assertEqual(max_length, 50)

    def test_phone_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('phone').max_length
        self.assertEqual(max_length, 11)

    def test_city_max_length(self):
        client = Client.objects.get(id=1)
        max_length = client._meta.get_field('city').max_length
        self.assertEqual(max_length, 20)


class ProjectModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        service = Service.objects.create(name='name', description='description')
        client = Client.objects.create(name='name', email='mail@mail.com', phone='99999999999', city='City-State')
        project = Project.objects.create(
            name='name',
            description='description',
            service=service,
            client=client,
            date=timezone.now(),
            url='site.com',
        )

    def test_name_max_length(self):
        project = Project.objects.get(id=1)
        max_length = project._meta.get_field('name').max_length
        self.assertEqual(50, max_length)

    def test_url_is_blank(self):
        project = Project.objects.get(id=1)
        is_blank = project._meta.get_field('url').blank
        self.assertEqual(True, is_blank)




