from django.test import TestCase
from sms_app.models import Stock, Tag


class TestStockModel(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            id=1,
            name='Furniture'
        )

        self.obj = Stock.objects.create(
            id=1,
            name='laptop',
            price=300,
            quantity=50,
            quantity_required=30,
            receive_quantity=20,

        )

    def test_stock_creating(self):
        self.assertEquals(self.obj.name, 'laptop')


    # test manytomany
