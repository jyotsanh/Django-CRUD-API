from rest_framework import serializers
from .models import Student

class StudentSerialzers(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    # This method is called when creating a new instance of the Student model
    # It takes in the validated data as a parameter and creates a new instance
    # of the Student model with the provided data.
    # The validated data is a dictionary that contains the data that has been
    # validated by the serializer.
    # The '**' operator is used to unpack the dictionary and pass the key-value
    def update(self, instance, validate_data):
        # Retrieve the value of the 'name' key from the validate_data dictionary.
        # If the key is not present in the dictionary, use the current value of the 'name' field in the instance of the Student model.
        # Update the 'name' field of the instance with the retrieved value.
        instance.name = validate_data.get('name', instance.name)
        
        # Retrieve the value of the 'roll' key from the validate_data dictionary.
        # If the key is not present in the dictionary, use the current value of the 'roll' field in the instance of the Student model.
        # Update the 'roll' field of the instance with the retrieved value.
        instance.roll = validate_data.get('roll', instance.roll)
        
        # Retrieve the value of the 'city' key from the validate_data dictionary.
        # If the key is not present in the dictionary, use the current value of the 'city' field in the instance of the Student model.
        # Update the 'city' field of the instance with the retrieved value.
        instance.city = validate_data.get('city', instance.city)
        
        # Save the updated instance of the Student model to the database.
        instance.save()
        
        # Return the updated instance of the Student model.
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
    
class StudentModelSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
    # This method is responsible for validating the roll field of the serializer
    # data before it is saved to the database. It checks if the roll number is
    # greater than 100 and raises a validation error if it is. If the roll number
    # is valid, it returns the validated data.
    def validate_roll(self, data):
        # Check if the roll number is greater than 100
        if data > 100:
            # If the roll number is greater than 100, raise a validation error
            # with an appropriate message.
            raise serializers.ValidationError(
                'Roll number should be less than 100'
            )
        # If the roll number is valid, return the validated data.
        return data
    # This method is responsible for validating the serializer data before it
    # is saved to the database. It checks if the name field contains the string
    # 'jyotsan' (case insensitive) and raises a validation error if it does.
    # If the name is valid, it returns the validated data.
    def validate(self, attrs):
        # Get the name field from the serializer data
        name = attrs.get('name')
        
        # Check if the name field contains the string 'jyotsan' (case insensitive)
        if name.lower() == 'jyotsan':
            # If the name is 'jyotsan', raise a validation error
            raise serializers.ValidationError('Jyotsan is not allowed')
        
        # If the name is valid, return the validated data
        return attrs
