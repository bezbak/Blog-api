from rest_framework import generics
from users.serilizers import UserSerializer, RegisterSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from users.models import User
# Create your views here.

class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
class UserAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer