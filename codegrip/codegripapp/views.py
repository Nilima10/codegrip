from django.shortcuts import render
from django.views.generic import View
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.contrib.auth import login as loginuser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.


class Home(View):
    def get(self,request):
        return render(request, 'home.html')

# login Class based view for login manager

class LoginAPI(APIView):
    def post(self, request):
        serilizer = LoginSerializer(data=request.data)
        if serilizer.is_valid():
            user = serilizer.validated_data['user']
            token, create = Token.objects.get_or_create(user=user)
            loginuser(request, user)
            return Response({'status':'1', 'Message':'You are login successfully', 'Token':token.key},status=200)

# Manager SignUp
class SignupAPI(APIView):
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create()
            user.set_password(serializer.validated_data['password'])
            user.username = serializer.validated_data['username']
            user.email = serializer.validated_data['email']
            user.first_name = serializer.validated_data['first_name']
            user.last_name = serializer.validated_data['last_name']
            user.is_manager = True
            user.save()
            manager = ManagerProperties.objects.create(user=user)
            manager.address = serializer.validated_data['address']
            manager.dob = serializer.validated_data['dob']
            manager.company = serializer.validated_data['company']
            manager.save()
            if user:
                return Response({'status':'1', 'Message':'You have Registered Succssfully'}, status=200)
            else:
                return Response({'status':'0', 'errors':serializer.errors}, status=200)
        return Response({'status':'0', 'Message':serializer.errors}, status=200)

class AddemployeeAPI(APIView):
    def post(self, request):
        serializer = AddemployeeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(email=serializer.validated_data['email'])
                return Response({'status':'0', 'Message':'Employee with this Email ID already Exist'}, status=200)
            except:
                user = User.objects.create()
                user.set_password(serializer.validated_data['password'])
                user.username = serializer.validated_data['username']
                user.email = serializer.validated_data['email']
                user.first_name = serializer.validated_data['first_name']
                user.last_name = serializer.validated_data['last_name']
                user.is_employee = True
                user.save()
                employee = EmployeeProperties.objects.create(user=user)
                employee.address = serializer.validated_data['address']
                employee.dob = serializer.validated_data['dob']
                employee.company = serializer.validated_data['company']
                employee.mobile = serializer.validated_data['mobile']
                employee.city = serializer.validated_data['city']
                employee.save()
                if user:
                    return Response({'status': '1', 'Message': 'Employee Added Succssfully'}, status=200)
                else:
                    return Response({'status': '0', 'errors': serializer.errors}, status=200)
        return Response({'status': '0', 'Message': serializer.errors}, status=200)


class GetemployeeAPI(APIView):
    def post(self, request):
        serializer = GetemployeeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(id=serializer.validated_data.get('user_id')[0].id)
                employee = EmployeeProperties.objects.get(user=user)
                data = {
                    'status':'1',
                    'username':employee.user.username,
                    'email':employee.user.email,
                    'first name':employee.user.first_name,
                    'last name':employee.user.last_name,
                    'address': employee.address,
                    'company': employee.company,
                    'Date of birth': employee.dob,
                    'mobile': employee.mobile,
                    'city':employee.city,

                }
                return Response(data, status=200)
            except:
                return Response({'status':'0', 'Message':'Employee Does not exist'}, status=200)
        return Response({'status':'0', 'Message':'Employee Does Not Exist'},status=200)

class EditemployeeAPI(APIView):
    def post(self, request):
        serializer = EditemployeeSerializer(data=request.data)
        if serializer.is_valid():
            try:
                print(serializer.validated_data.get('user_id'))
                user = User.objects.get(id=serializer.validated_data.get('user_id')[0].id)
                print(user)
                print(user.username)
                user.username = serializer.validated_data['username']
                print(user.username)
                user.first_name = serializer.validated_data['first_name']
                print(user.first_name)
                user.last_name = serializer.validated_data['last_name']
                user.email = serializer.validated_data['email']
                user.save()
                employee = EmployeeProperties.objects.get(user=user)
                print(employee)
                employee.address = serializer.validated_data['address']
                employee.dob = serializer.validated_data['dob']
                employee.company = serializer.validated_data['company']
                employee.mobile = serializer.validated_data['mobile']
                employee.city = serializer.validated_data['city']
                employee.save()
                return Response({'status':'1', 'Message':'Employee Details Updated successfully'}, status=200)
            except:
                return Response({'status':'0', 'Message':'Employee Does Not exists'}, status=200)

class DeletemployeeAPI(APIView):
    def post(self, request):
        serializer = DeleteSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(id=serializer.validated_data.get('user_id')[0].id)
            user.delete()
            return Response({'status':'1', 'Message':'Employee Deleted Successfully'}, status=200)
        else:
            return Response({'status':'0', 'Message':'Employee Does Not Exist'}, status=200)