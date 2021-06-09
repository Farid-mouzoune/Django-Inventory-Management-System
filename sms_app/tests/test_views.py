from django.test import TestCase, Client
from django.urls import reverse
from sms_app.views import Stock, Tag
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.all_stock_url = reverse('sms_app:all_stock')
        self.get_stock_url = reverse('sms_app:get_stock', args=['3'])
        self.obj3 = Stock.objects.create(
            id=3,
            name='sony',
            quantity=10,
            quantity_required=20,
            receive_quantity=12,
        )

    def test_stock_list_get(self):
        response = self.client.get(self.all_stock_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sms_app/all_stock.html')

    def test_stock_detail_get(self):
        response = self.client.get(self.get_stock_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sms_app/get_stock.html')
