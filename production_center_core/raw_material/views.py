from rest_framework.viewsets import ModelViewSet

from .models import RawMaterial
from .serializers import RawMaterialSerializer


class RawMaterialViewSet(ModelViewSet):
    serializer_class = RawMaterialSerializer
    queryset = RawMaterial.objects.all()
