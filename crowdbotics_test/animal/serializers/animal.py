from rest_framework import serializers
from crowdbotics_test.animal.models import Animal


class AnimalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = '__all__'
