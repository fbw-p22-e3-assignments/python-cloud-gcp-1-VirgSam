from rest_framework import serializers
from .models import Todo, Contact

# Import Validation classes from rest framework
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

class TodoSerializer(serializers.ModelSerializer):
    """Processes the model into JSON using the defined fields"""
    class Meta:
        model = Todo
        fields = ['task', 'details', 'completed']
        
        
class ContactSerializer(serializers.Serializer):
    name = serializers.CharField()
    phone_number = serializers.CharField(validators=[
        # This validator must be added to the serializer field directly
        UniqueValidator(queryset=Contact.objects.all(),
                        message="Phone number already entered")
        ])
    email = serializers.EmailField(validators=[
        UniqueValidator(queryset=Contact.objects.all(),
                        message="Email is already used")
    ])
    
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Contact.objects.all(),
                # The fields must exist as fields in the serializer class
                fields=['name', 'phone_number'],
                # optional argument
                message="No Phone number can have 2 different names"
            )
        ]
    
    # Used mainly for the basic Serializer class or custom use cases
    def create(self, validated_data):
        """Create a new Contact object after data has been validated"""
        return Contact.objects.create(**validated_data)
        