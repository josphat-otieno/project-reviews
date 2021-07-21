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

class TestProject(TestCase):
    def setUP(self):
        self.josphat = UserProfile(profile_photo='swimming.jpg', bio = 'okay',phone_number = 717878813, user = User(username = 'jose', password ='jose45'))
        self.josphat.save_profile()

        self.new_project = Project(project_title = 'instagram', project_image='simming.jpg', project_description='okay', project_link='https://jose-awards.herokuapp.com/', user = self.josphat)
        self.new_project.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_project, Project))


    def test_save_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_method(self):
        self.new_project.save_project()
        projects = Project.objects.all()
        self.new_project.delete_project()
        self.assertTrue(len(projects)==0)

class TestRating(TestCase):
    def setUp(self):
        self.josphat = UserProfile(profile_photo='swimming.jpg', bio = 'okay',phone_number = 717878813, user = User(username = 'jose', password ='jose45'))
        self.josphat.save_profile()

        self.new_project = Project(project_title = 'instagram', project_image='simming.jpg', project_description='okay', project_link='https://jose-awards.herokuapp.com/', user = self.josphat)
        self.new_project.save()

        self.rating = Rating(design=2, usability=3, content=4, user = self.josphat, project=self.new_project)
        self.rating.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_method(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating)>0)