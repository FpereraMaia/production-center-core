from rest_framework.viewsets import ModelViewSet

from .models import RawMaterial
from .serializers import RawMaterialSerializer


class RawMaterialViewSet(ModelViewSet):
    """
     retrieve:
         Return the given Raw Material.

     list:
         Return a list of all Raw Material.

     create:
         Create a new raw material.

     destroy:
         Delete a Raw Material.

     update:
         Update a Raw Material.

     partial_update:
         Update a Raw Material.
     """

    serializer_class = RawMaterialSerializer
    queryset = RawMaterial.objects.all()
