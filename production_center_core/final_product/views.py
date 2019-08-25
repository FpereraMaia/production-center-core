from rest_framework.viewsets import ModelViewSet

from .models import FinalProduct
from .serializers import FinalProductSerializer


class FinalProductViewSet(ModelViewSet):
    serializer_class = FinalProductSerializer
    queryset = FinalProduct.objects.all()
