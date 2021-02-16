from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError
# Custome authentication for email authentication
def authenticate(username=None, password=None):
    try:
        user = User.objects.get(email=username)
    except User.DoesNotExist:
        return None
    else:
        if user.check_password(password):
            return user
    return None

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self,data):
        username = data.get('email', '')
        password = data.get('password', '')
        if username != '' and password != '':
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    data['user'] = user
                else:
                    raise ValidationError('User not active')
            else:
                raise ValidationError('unable to login')
        else:
            raise ValidationError('Please Enter Valid username and password')
        return data


class SignupSerializer(serializers.ModelSerializer):
    address = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)
    company = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email','password','first_name', 'last_name', 'company', 'dob', 'address']

        extra_kwargs = {
            'password':{'write_only':True}
        }

        # def save(self):
        #     user = User(
        #         email = self.validated_data['email'],
        #         username=self.validated_data['username'],
        #         first_name=self.validated_data['first_name'],
        #         last_name=self.validated_data['last_name'],
        #         is_manager=True,
        #     )
        #     password = self.validated_data['password']
        #     password2 = self.validated_data['password2']
        #     print(password2)
        #     if password == password2:
        #         user.set_password(password)
        #     user.save()
        #     return user

class AddemployeeSerializer(serializers.ModelSerializer):
    address = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)
    company = serializers.CharField(required=False)
    mobile = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'company', 'dob', 'address', 'mobile','city']

        extra_kwargs = {
            'password': {'write_only': True}
        }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class GetemployeeSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

class EditemployeeSerializer(serializers.Serializer):
    # user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())
    address = serializers.CharField(required=False)
    dob = serializers.DateField(required=False)
    company = serializers.CharField(required=False)
    mobile = serializers.CharField(required=False)
    city = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['user_id','username', 'email','first_name', 'last_name', 'company', 'dob', 'address', 'mobile','city']

class DeleteSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())