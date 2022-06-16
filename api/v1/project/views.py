from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializer import ProjectSerialzer
from rest_framework.generics import GenericAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from blog.models import Project
from django.http import Http404


class ProjectView(GenericAPIView):
    serializer_class = ProjectSerialzer
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            return Http404


    def get(self, request, pk=None, *args, **kwargs):
        response = self.get_object(pk)
        serializer = ProjectSerialzer(response)
        return Response(serializer.data, status=HTTP_200_OK, content_type='application/json')


class ProjectListView(ListAPIView):
    serializer_class = ProjectSerialzer
    queryset = Project.objects.all()
