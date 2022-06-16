from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializer import CategorySerialzer
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from blog.models import Category
from django.http import Http404


class CategoryView(GenericAPIView):
    serializer_class = CategorySerialzer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Http404


    def get(self, request, pk=None, *args, **kwargs):
        response = self.get_object(pk)
        serializer = CategorySerialzer(response)
        return Response(serializer.data, status=HTTP_200_OK, content_type='application/json')


class CategoryListView(ListAPIView):
    serializer_class = CategorySerialzer
    queryset = Category.objects.all()
