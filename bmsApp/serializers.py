from .models import Client, History
from rest_framework import serializers

def no_update_with_value(value):
    def validate_no_update(value):
        if value == 'verified':
            raise serializers.ValidationError("Updating attribute with this value is not allowed.")
    return validate_no_update
from django.core.exceptions import ValidationError
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
        
    def validate_status(self, value):
        if self.instance and self.instance.status == 'verified':
            raise ValidationError("Updating status with verified user is not allowed.")
        
        return value
class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'