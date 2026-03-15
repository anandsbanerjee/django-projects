from rest_framework import serializers

from .models import Weather


class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    temperature_celsius = serializers.FloatField()
    temperature_fahrenheit = serializers.SerializerMethodField() # computed read only field
    condition = serializers.ChoiceField(
        choices=["Sunny", "Rainy", "Cloudy", "Snowy"])

    def get_temperature_fahrenheit(self, obj):
        cels =  obj.get("temperature_celsius")
        return cels * (9/5) + 32



class TodoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    completed = serializers.BooleanField(default=False)

    # Validate title has atleast 3 characters
    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "Title must be at least 3 characters long."
            )
        return value