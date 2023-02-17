from rest_framework import serializers
from .models import Twittes, TwittesMedia, Like, Comment
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


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    twittes = TwittesSerializer(read_only=True)

    class Meta:
        model = Like
        fields = '__all__'


class CreateLikeSerializer(serializers.Serializer):
    twittes = serializers.PrimaryKeyRelatedField(
        queryset=Twittes.objects.all()
    )

    def validate(self, attrs):
        user = self.context['request'].user
        if Like.objects.filter(user=user, twittes=attrs['twittes']).exists():
            raise serializers.ValidationError(
                {'like': 'you liked this twittes'})
        return attrs

    def create(self, validated_data):
        user = self.context['request'].user
        obj = Like.objects.create(
            user=user,
            twittes=validated_data['twittes']
        )
        return obj
