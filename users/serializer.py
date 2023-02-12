from rest_framework import serializers
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ('password',)


class SignUpUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=50, write_only=True)

    def validate_username(self, value):
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError('this username is taken')
        return value

    def process(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

    def save(self, **kwargs):
        self.process(self.validated_data)


class SignInUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=50, write_only=True)

    def validate_username(self, value):
        if not get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError('this username is not exists')
        return value
