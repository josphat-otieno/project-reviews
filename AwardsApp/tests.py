from django.test import TestCase
from .models import UserProfile, Project, Rating, User
# Create your tests here.

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username = 'jose', password ='jose45')
        self.user.save()
        self.josphat = UserProfile(profile_photo='swiiming.jpg', bio = 'okay', phone_number = 717878813, user = self.user)
        self.josphat.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.josphat, UserProfile))

    def test_save_method(self):
        self.josphat.save_profile()
        profile = UserProfile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.josphat.save_profile()
        profile = UserProfile.objects.all()
        self.josphat.delete_profile()
        self.assertTrue(len(profile)==0)



        