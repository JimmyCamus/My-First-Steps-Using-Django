from rest_framework import serializers


class PersonSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    rut = serializers.CharField(max_length=12)


class PetSerializer(serializers.Serializer):
    species = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    color = serializers.CharField(max_length=50)
