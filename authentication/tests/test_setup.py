from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker 

class TestSetUp(APITestCase):
    def setUp(self) -> None:
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.fake = Faker()
        
        self.user_data={
            'email': self.fake.email(),
            'first_name': "John",
            'last_name': "Doe",
            'password': "password"
        }
        
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown() 