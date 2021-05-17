from django.test import TestCase
from ..models import Contact


class ContactTest(TestCase):
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
