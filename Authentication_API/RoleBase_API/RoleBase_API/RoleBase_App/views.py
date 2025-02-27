from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics


UserLogin_Model = get_user_model()


class SignUpUserView(APIView):
    def post(self, request):
        data = request.data.copy()
        serializer = UserSerializer(data=data)
        data['role'] = 'user'
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    def post(self, request):
        input_username = request.data.get('username')
        input_password = request.data.get('password')

        if not input_username or not input_password:
            return Response({'message': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=input_username, password=input_password)
        if user is None:
            return Response({'message': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        refresh['role'] = user.role 
        return Response({
            'message': 'Login successful',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'role': user.role,
        }, status=status.HTTP_200_OK)


class ShowUserView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response(
                {"message": "Authorization header is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            access_token_str = auth_header.split(" ")[1]
        except IndexError:
            return Response(
                {"message": "Invalid Authorization header format. Expected 'Bearer <token>'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        

        try:
            validated_token = AccessToken(access_token_str)
        except TokenError:
            return Response(
                {"message": "Invalid access token"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user_id_from_token = validated_token.get('role')
        if user_id_from_token != 'admin':    
            return Response(
                {"message": "Token does not belong to the authenticated admin"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        print("Extracted user ID from token:", user_id_from_token)

        all_users = UserLogin_Model.objects.all()  
        
        serializer = UserSerializer(all_users, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class CreateUserView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response(
                {"message": "Authorization header is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            access_token_str = auth_header.split(" ")[1]
        except IndexError:
            return Response(
                {"message": "Invalid Authorization header format. Expected 'Bearer <token>'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        

        try:
            validated_token = AccessToken(access_token_str)
        except TokenError:
            return Response(
                {"message": "Invalid access token"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user_id_from_token = validated_token.get('role')
        if user_id_from_token != 'admin':    
            return Response(
                {"message": "Token does not belong to the authenticated admin"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        print("Extracted user ID from token:", user_id_from_token)

        
        data = request.data.copy()
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HistoryUsersView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = UserSerializer

    def get(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return Response(
                {"message": "Authorization header is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            access_token_str = auth_header.split(" ")[1]
        except IndexError:
            return Response(
                {"message": "Invalid Authorization header format. Expected 'Bearer <token>'."},
                status=status.HTTP_400_BAD_REQUEST
            )
        

        try:
            validated_token = AccessToken(access_token_str)
        except TokenError:
            return Response(
                {"message": "Invalid access token"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        user_id_from_token = validated_token.get('role')
        if user_id_from_token != 'manager':    
            return Response(
                {"message": "Token does not belong to the authenticated manager"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        print("Extracted user ID from token:", user_id_from_token)
    
        queryset = UserLogin_Model.objects.all()

        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        
        if start_date and end_date:
            queryset = queryset.filter(date__range=[start_date, end_date])
        elif start_date:
            queryset = queryset.filter(date__gte=start_date)
        elif end_date:
            queryset = queryset.filter(date__lte=end_date)

        if start_time and end_time:
            queryset = queryset.filter(time__range=[start_time, end_time])
        elif start_time:
            queryset = queryset.filter(time__gte=start_time)
        elif end_time:
            queryset = queryset.filter(time__lte=end_time)
        

        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    