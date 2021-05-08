from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import CurriculumSerializer
from .models import Curriculum

# Create your views here.
class CurriculumViewSet(viewsets.ModelViewSet):
    """
    A viewset for create, viewing and editing customer instances.
    """

    permission_classes = (IsAuthenticated,)
    serializer_class = CurriculumSerializer
    queryset = Curriculum.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
