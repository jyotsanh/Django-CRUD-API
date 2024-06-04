from rest_framework import serializers
from .models import Student

class StudentSerialzers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    def create(self,validate_data):
        return Student.objects.create(**validate_data)
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.roll = validate_data.get('roll',instance.roll)
        instance.city = validate_data.get('city',instance.city)
        instance.save()
        return instance
    # field level validation
    def validate_roll(self,data):
        None
    # object level validation
    def validate(self, attrs):
        name = attrs.get('name')
        if name.lower() == 'jyotsan':
            raise serializers.ValidationError('Jyotsan is not allowed')
        return attrs