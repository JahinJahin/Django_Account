from medicine.models import medicine
from rest_framework import serializers

class medicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = medicine
        fields=['name','cost','shop','adress']