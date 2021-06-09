from django.test import SimpleTestCase
from django.urls import reverse, resolve
from sms_app.views import all_stock, get_stock, add_stock, update_stock, delete_stock


class TestUrls(SimpleTestCase):

    def test_all_stock_urls_is_resolved(self):
        url = reverse('sms_app:all_stock')
        print(resolve(url))
        self.assertEquals(resolve(url).func, all_stock)

    def test_add_stock_urls_is_resolved(self):
        url = reverse('sms_app:add_stock')
        print(resolve(url))
        self.assertEquals(resolve(url).func, add_stock)

    def test_get_stock_urls_is_resolved(self):
        url = reverse('sms_app:get_stock', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, get_stock)

    def test_update_stock_urls_is_resolved(self):
        url = reverse('sms_app:update_stock', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, update_stock)

    def test_delete_stock_urls_is_resolved(self):
        url = reverse('sms_app:delete_stock', args=[1])
        print(resolve(url))
        self.assertEquals(resolve(url).func, delete_stock)
