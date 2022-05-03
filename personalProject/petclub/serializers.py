from rest_framework import serializers

from .models import(
    Person,
    Pet,
)


class PersonSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    email = serializers.EmailField(max_length=255)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    rut = serializers.CharField(max_length=12)

    class Meta:
        model = Person

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get(
            'first_name', instance.first_name)
        instance.last_name = validated_data.get(
            'last_name', instance.last_name)
        instance.rut = validated_data.get('rut', instance.rut)
        instance.save()
        return instance


class PetSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    species = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    color = serializers.CharField(max_length=50)

    class Meta:
        model = Pet

    def create(self, validated_data):
        return Pet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.species = validated_data.get('species', instance.species)
        instance.name = validated_data.get(
            'name', instance.name)
        instance.age = validated_data.get(
            'age', instance.age)
        instance.color = validated_data.get('color', instance.color)
        instance.save()
        return instance
