from rest_framework import serializers
from .models import Twittes, TwittesMedia
from users.serializer import UserSerializer


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwittesMedia
        fields = '__all__'


class TwittesSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    media = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Twittes
        fields = '__all__'

    def get_media(self, instance):
        media = TwittesMedia.objects.filter(twittes__pk=instance.pk)
        return MediaSerializer(media, many=True).data


class CreateTwittesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twittes
        exclude = ('user',)

    def create(self, validated_data):
        request = self.context['request']
        twittes = Twittes.objects.create(user=request.user, **validated_data)
        for name, file in request.FILES.items():
            TwittesMedia.objects.create(
                twittes=twittes,
                media=file,
            )
        return twittes


class RetrieveUpdateDestroyTwittesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Twittes
        exclude = ('user',)
