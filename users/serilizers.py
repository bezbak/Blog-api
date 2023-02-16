from rest_framework import serializers
from users.models import User
from posts.serializers import PostSerializer

class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only= True, max_length = 255)
    password = serializers.CharField(write_only= True, max_length = 255)
    confirm_password = serializers.CharField(write_only= True, max_length = 255)
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
    def vallidate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        return attrs
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        return user

class UserSerializer(serializers.ModelSerializer):
    post_user = PostSerializer(many = True, read_only=True)
    class Meta():
        model = User
        fields = ('id', 'username', 'first_name', 'post_user', 'last_name', 'profile_image')