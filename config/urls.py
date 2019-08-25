"""production_center_core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from production_center_core.raw_material.views import RawMaterialViewSet
from production_center_core.employee.views import EmployeeViewSet
from production_center_core.final_product.views import FinalProductViewSet

app_name = "production_center_core"
schema_view = get_swagger_view(title="Production Center API")

router = routers.DefaultRouter()
router.register(r"raw-materials", RawMaterialViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"final-products", FinalProductViewSet)

urlpatterns = [path("docs", schema_view), path("api/v1/", include(router.urls, None))]
