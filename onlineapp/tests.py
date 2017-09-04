from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from onlineapp.models import College,Student

class College_Tests(APITestCase):
    def test_create(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('onlineapp:collegelist')
        data = {"name": "HITAM college of engineering", "location": "Hyderabad", "acronym": "hitam",
                "contact": "contact@hitam.com"}
        response = self.client.put(url + '1/', data, format='json')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(url + '1/')
      #  for i in data:
       #     self.assertEqual(response.json()[i], data[i])
        self.assertEqual(response.json(), data)
        #response = self.client.delete(url, data, format='json')
       # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    ''' url=reverse('onlineapp:collegelist')
        data={"name":"HITAM college","location":"Hyderabad","acronym":"hitam","contact":"contact@hitam.com"}
        response=self.client.post(url,data,format='json')
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        response=self.client.get(url+'1/')
        for i in data:
            self.assertEqual(response.json()[i],data[i])'''


