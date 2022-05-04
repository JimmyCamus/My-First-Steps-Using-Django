from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers

from .models import(
    Person,
    Pet,
)


class HelloWorld(APIView):
    def get(self, request):
        return Response({'data': 'Hello World'}, status=status.HTTP_200_OK)


class PersonAPIWiew(APIView):
    serializer_class = serializers.PersonSerializer

    def get(self, request):
        persons = Person.objects.all().values()
        return Response({'data': persons}, status=status.HTTP_200_OK)

    def post(self, request):
        new_person = self.serializer_class(data=request.data)
        if not new_person.is_valid():
            return Response(
                new_person.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        new_person.save()
        return Response({'data': new_person.data}, status=status.HTTP_201_CREATED)

    def patch(self, request):
        if 'id' not in request.data.keys():
            return Response(
                {'id': ['This field is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        client_id = request.data['id']

        try:
            person = Person.objects.get(id=client_id)
            serialized_person = self.serializer_class(person, request.data)
            if not serialized_person.is_valid():
                return Response(
                    serialized_person.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            serialized_person.save()
            return Response({'data': serialized_person.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({'id': [f'There is not a Person with id {client_id}']}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.data.keys():
            return Response(
                {'id': ['This field is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        client_id = request.data['id']

        try:
            person = Person.objects.get(id=client_id)
            serialized_person = serializers.PersonSerializer(person)
            person.delete()
            return Response({'data': serialized_person.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'id': [f'There is not a Person with id {client_id}']})


class PetAPIWiew(APIView):
    serializer_class = serializers.PetSerializer

    def get(self, request):
        pets = Pet.objects.all().values()
        return Response({'data': pets}, status=status.HTTP_200_OK)

    def post(self, request):
        new_pet = self.serializer_class(data=request.data)
        if not new_pet.is_valid():
            return Response(
                new_pet.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        new_pet.save()
        return Response({'data': new_pet.data}, status=status.HTTP_201_CREATED)

    def patch(self, request):
        if 'id' not in request.data.keys():
            return Response(
                {'id': ['This field is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        client_id = request.data['id']

        try:
            pet = Pet.objects.get(id=client_id)
            serialized_pet = self.serializer_class(pet, request.data)
            if not serialized_pet.is_valid():
                return Response(
                    serialized_pet.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )
            serialized_pet.save()
            return Response({'data': serialized_pet.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({'id': [f'There is not a Person with id {client_id}']}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.data.keys():
            return Response(
                {'id': ['This field is required.']},
                status=status.HTTP_400_BAD_REQUEST
            )
        client_id = request.data['id']

        try:
            pet = Pet.objects.get(id=client_id)
            serialized_pet = serializers.PetSerializer(pet)
            pet.delete()
            return Response({'data': serialized_pet.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({'id': [f'There is not a Person with id {client_id}']})
