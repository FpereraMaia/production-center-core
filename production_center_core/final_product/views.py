from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import FinalProduct
from .serializers import FinalProductSerializer
from .services import FinalProductService


class FinalProductViewSet(ModelViewSet):
    serializer_class = FinalProductSerializer
    queryset = FinalProduct.objects.all()

    def partial_update(self, request, *args, **kwargs):
        final_product = FinalProductService.get_by_id(kwargs.get("pk", None))
        final_product = FinalProductService.partial_update(final_product, request.data)
        return Response(FinalProductSerializer(final_product).data)
