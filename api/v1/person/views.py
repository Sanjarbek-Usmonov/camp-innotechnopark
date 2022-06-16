from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializer import PersonSerialzer
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from blog.models import Person
from django.http import Http404


class PersonView(GenericAPIView):
    serializer_class = PersonSerialzer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            return Http404


    def get(self, request, pk=None, *args, **kwargs):
        response = self.get_object(pk)
        serializer = PersonSerialzer(response)
        return Response(serializer.data, status=HTTP_200_OK, content_type='application/json')


class PersonListView(ListAPIView):
    serializer_class = PersonSerialzer
    queryset = Person.objects.all()
