from rest_framework import generics, permissions, filters
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # Backend filtering / sorting / searching
    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter,
    ]

    # Exact-match filters
    filterset_fields = [
        "product_category",
        "product_manufacturing_date",
        "product_expiry_date",
    ]

    # Sorting
    ordering_fields = [
        "product_price",
        "product_manufacturing_date",
        "product_expiry_date",
    ]

    ordering = ["product_id"]  # default ordering

    # Search
    search_fields = [
        "product_id",
        "product_category",
    ]

class ProductCategoryListAPIView(APIView):
    def get(self, request):
        categories = (
            Product.objects
            .values_list("product_category", flat=True)
            .distinct()
        )
        return Response(categories)