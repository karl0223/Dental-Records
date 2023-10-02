from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseCreateSerializer

class UserCreateSerializer(BaseCreateSerializer):
    class Meta(BaseCreateSerializer.Meta):              # Inherit the Meta class of BaseCreateSerializer
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']