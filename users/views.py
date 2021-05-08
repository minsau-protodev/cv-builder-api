from rest_framework.generics import RetrieveAPIView, CreateAPIView
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import UserSerializer, RegisterSerializer

# Create your views here.
class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
