from .serializer import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication


UserLogin_Model = get_user_model()


class RegisterUserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'User created successfully',
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
    def get(self, request):
        users = UserLogin_Model.objects.all()  
        serializer = UserSerializer(users, many=True)  
        return Response(serializer.data, status=status.HTTP_200_OK)    
        

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
        return Response({
            'message': 'Login successful',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)


class RefreshAndVerifyTokenView(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"message": "Refresh token is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)

            access_token = str(refresh.access_token)

            try:
                return Response({
                    "message": "Token is valid",
                    "new_access_token": access_token
                }, status=status.HTTP_200_OK)

            except TokenError:
                return Response({"message": "Invalid access token"}, status=status.HTTP_401_UNAUTHORIZED)

        except TokenError:
            return Response({"message": "Invalid refresh token"}, status=status.HTTP_401_UNAUTHORIZED)


class AuthenticationTokenHeaderView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        input_username = request.data.get('username')
        input_password = request.data.get('password')
        
        if not input_username or not input_password:
            return Response(
                {"message": "Username and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        user = authenticate(request, username=input_username, password=input_password)
        if user is None:
            return Response(
                {"message": "Invalid username or password"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        

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
        
        user_id_from_token = validated_token.get('user_id')
        
        if user_id_from_token != user.id:
            return Response(
                {"message": "Token does not belong to the authenticated user"},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        print("Extracted user ID from token:", user_id_from_token)

        return Response(
            {"message": "User authenticated successfully"},
            status=status.HTTP_200_OK
        )


