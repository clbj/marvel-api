from django.test import TestCase
from api.models.user import User

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(name="TestUser")

    
    def test_user_creation(self):
        myuser = User.objects.get(name="TestUser")
        self.assertEqual(str(myuser), "I'm TestUser")