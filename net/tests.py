import datetime

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from net.models import Product, Organization, Contact
from users.models import User


# Create your tests here.
class OrganizationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create(email='test@mail.ru', password='test', is_active=True)
        self.client.force_authenticate(user=self.user)
        self.organization_factory = Organization.objects.create(name='test', organization_type='factory', creation_date='2024-01-16')
        self.organization_net = Organization.objects.create(name='test_net', organization_type='net', supplier=self.organization_factory, debt='1245.13', creation_date='2024-01-16')
        self.product = Product.objects.create(name='test', model='test', launch_date='2024-01-15', organization=self.organization_factory)
        self.contact = Contact.objects.create(email='test@test.ru', country='test', city='test', street_name='test', number='test', organization=self.organization_factory)

        self.maxDiff=None
    def test_create_organization(self):
        data = {
            "name": "test",
            "organization_type": "factory",
        }

        response = self.client.post(
            reverse('net:organization_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Organization.objects.all().exists()
        )

    def test_organization_delete(self):
        response = self.client.delete(
            reverse('net:organization_destroy', args=[self.organization_factory.pk])
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_organization_update(self):
        response = self.client.patch(
            reverse('net:organization_update', args=[self.organization_factory.pk]),
            data={'name': 'updated'}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        response = self.client.patch(
            reverse('net:organization_update', args=[self.organization_factory.pk]),
            data={'debt': 1234.25}
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(), {"name": 'updated', 'creation_date': datetime.date.strftime(self.organization_factory.creation_date, '%Y-%m-%d'), 'debt': None, 'organization_type': 'factory', 'supplier': None, "id": self.organization_factory.pk}
        )

    def test_organization_list(self):
        response = self.client.get(
            reverse('net:organization_list')
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            [{
                "id": self.organization_factory.pk,
                "name": self.organization_factory.name,
                "organization_type": self.organization_factory.organization_type,
                "debt": self.organization_factory.debt,
                "creation_date": datetime.date.strftime(self.organization_factory.creation_date, '%Y-%m-%d'),
                "supplier": None
            },
                {
                    "id": self.organization_net.pk,
                    "name": self.organization_net.name,
                    "organization_type": self.organization_net.organization_type,
                    "debt": self.organization_net.debt,
                    "creation_date": datetime.date.strftime(self.organization_net.creation_date, '%Y-%m-%d'),
                    "supplier": self.organization_net.supplier.pk
                }]
        )

    def test_detail_organization(self):
        response = self.client.get(
            reverse('net:organization_retrieve', args=[self.organization_factory.pk]),
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        print(response.json())
        self.assertEquals(
            response.json(),
            {
                "id": self.organization_factory.pk,
                "products": [
                    {
                        "id": self.product.pk,
                        "name": self.product.name,
                        "model": self.product.model,
                        "launch_date": self.product.launch_date,
                        "organization": self.product.organization.pk
                    }
                ],
                "contacts": [
                    {
                        "id": self.contact.pk,
                        "email": self.contact.email,
                        "country": self.contact.country,
                        "city": self.contact.city,
                        "street_name": self.contact.street_name,
                        "number": self.contact.number,
                        "organization": self.contact.organization.pk
                    }
                ],
                "name": self.organization_factory.name,
                "organization_type": self.organization_factory.organization_type,
                "debt": self.organization_factory.debt,
                "creation_date": datetime.datetime.strftime(self.organization_factory.creation_date, '%Y-%m-%d'),
                "supplier": self.organization_factory.supplier
            }
        )

    def test_active_user(self):
        self.user.is_active=False
        self.user.save()
        self.client.force_authenticate(user=self.user)

        data = {
            "name": "test",
            "organization_type": "factory",
        }

        response = self.client.post(
            reverse('net:organization_create'),
            data=data
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )