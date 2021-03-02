from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_With_email(self):
        
        email = "test@test.com" 
        password = "Test123"

        user = get_user_model().objects.create_user(
                email = email,
                password = password

        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    #To Normalize Email Address
    def test_new_user_email_normalized(self):
        email = "test@TEST.COM"
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email , email.lower())

    #Testing Email
    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                None, "Test123"

            )
    # Creating Super User
    def test_create_new_superuser(self):
         user = get_user_model().objects.create_superuser(
             "test1@test.com",
             "Test123"

         )

         self.assertTrue(user.is_superuser)
         self.assertTrue(user.is_staff)


