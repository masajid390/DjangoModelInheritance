from .animal import AnimalSerializer
from crowdbotics_test.animal.models import Dog


class DogSerializer(AnimalSerializer):

    def create(self, validated_data):
        return Dog.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.birthday = validated_data.get('birthday', instance.birthday)
        instance.save()
        return instance
