from django.test import TestCase
from .models import Location, Category, photos

# Create your tests here.

# location model tests
class LocationTestCase(TestCase):

    def setUp(self):
        """
        Create a location for testing
        """
        Location.objects.create(name="Test Location")

    def test_my_location(self):
        """
        Test that the location name is correct
        """
        location = Location.objects.get(name="Test Location")
        self.assertEqual(location.name, "Test Location")

    def test_location_str(self):
        """
        Test that the location string representation is correct
        """
        location = Location.objects.get(name="Test Location")
        self.assertEqual(str(location), "Test Location")


# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        """
        Create a category for testing
        """
        Category.objects.create(name="Test Category")

    def test_category_name(self):
        """
        Test that the category name is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category(self):
        """
        Test that the category string representation is correct
        """
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")


# image model tests
class ImageTestCase(TestCase):

    def setUp(self):
        """
        Create a image for testing
        """
        photos.objects.create(
            pic_name="Test Image",
            description="Test Description",
            location=Location.objects.create(name="Test Location"),
            category=Category.objects.create(name="Test Category"),
            image="https://avatars.mds.yandex.net/i?id=6ad815dc6169bc81d72aa57b7ca5a596-4893557-images-thumbs&n=13",
            created_at=None
        )

    def test_Photos_name(self):
        """
        Test that the image name is correct
        """
        Photos = photos.objects.get(name="Test Image")
        self.assertEqual(Photos.pic_name, "Test Image")

    def test_image_description(self):
        """
        Test that the image description is correct
        """
        Photos = photos.objects.get(name="Test Image")
        self.assertEqual(photos.description, "Test Description")

    def test_image_location(self):
        """
        Test that the image location is correct
        """
        Photos = photos.objects.get(name="Test Image")
        self.assertEqual(photos.location.name, "Test Location")

    def test_image_category(self):
        """
        Test that the image category is correct
        """
        Photos = photos.objects.get(name="Test Image")
        self.assertEqual(photos.category.name, "Test Category")

    def test_photos_photos(self):
        """
        Test that the image image is correct
        """
        Photos = photos.objects.get(name="Test Image")
        self.assertEqual(Photos.Photos, "https://avatars.mds.yandex.net/i?id=6ad815dc6169bc81d72aa57b7ca5a596-4893557-images-thumbs&n=13")


    def test_image_str(self):
        """
        Test that the image string representation is correct
        """
        Photos = photos.objects.get(name="Test Image")
        self.assertEqual(Photos.Photos, "https://avatars.mds.yandex.net/i?id=6ad815dc6169bc81d72aa57b7ca5a596-4893557-images-thumbs&n=13")