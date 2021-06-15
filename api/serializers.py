from rest_framework import serializers
from sms_app.models import Stock


class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'
