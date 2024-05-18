from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Vendor, PurchaseOrder

class VendorAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor_data = {
            'name': 'Test Vendor',
            'contact_details': 'test@example.com',
            'address': '123 Test Street',
            'vendor_code': 'VENDOR001',
        }
        self.vendor = Vendor.objects.create(**self.vendor_data)
        self.url = reverse('vendor-list')

    def test_create_vendor(self):
        response = self.client.post(self.url, self.vendor_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendor.objects.count(), 2)  # Check if a new vendor is created

    def test_retrieve_vendors(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if the number of vendors returned is correct

class PurchaseOrderAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name='Test Vendor',
            contact_details='test@example.com',
            address='123 Test Street',
            vendor_code='VENDOR001',
        )
        self.po_data = {
            'po_number': 'PO001',
            'vendor': self.vendor.id,
            'items': {'item1': 10, 'item2': 20},
            'quantity': 30,
        }
        self.po = PurchaseOrder.objects.create(**self.po_data)
        self.url = reverse('purchaseorder-list')

    def test_create_purchase_order(self):
        response = self.client.post(self.url, self.po_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(PurchaseOrder.objects.count(), 2)  # Check if a new purchase order is created

    def test_retrieve_purchase_orders(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Check if the number of purchase orders returned is correct
