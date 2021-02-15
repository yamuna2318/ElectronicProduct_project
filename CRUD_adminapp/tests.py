from django.test import TestCase
from .models import *

# Create your tests here.
class mobilesdataTestcase(TestCase):
    def setUp(self):
        mobilesdata.objects.create(screensize='6.2', color= 'Marbleblue')
        mobilesdata.objects.create(screensize='6.4', color='Grey')

    def test_mobile_test(self):
        obj1= mobilesdata.objects.get(screensize='6.2', color= 'Marbleblue')
        obj2=mobilesdata.objects.get(screensize='6.4', color='Grey')
        self.assertEqual(obj1.screensize,"6.2")
        self.assertEqual(obj2.screensize,"6.4")
