from rest_framework import serializers
from .models import Twittes
from users.serializer import UserSerializer


class TwittesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Twittes
        fields = '__all__'


class CreateTwittesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twittes
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context['request'].user
        obj = Twittes.objects.create(user=user, **validated_data)
        return obj


class RetrieveUpdateDestroyTwittesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twittes
        exclude = ('user',)
