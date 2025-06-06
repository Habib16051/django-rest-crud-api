from rest_framework.views import APIView
from .models import Travel
from .serializers import TravelSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import permissions
# Now we can use Mixins to create Class Based Views more easily
from rest_framework import status
from django.http import Http404
from rest_framework import mixins
from rest_framework import generics
from django.contrib.auth.models import User
from app_classviews.permissions import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.decorators import api_view

class TravelHighlight(generics.GenericAPIView):
    queryset = Travel.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        travel = self.get_object()
        return Response(travel.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'travels': reverse('travel-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# More Specified Views for the Travel model using Mixins and Generic Views
# It's the list view to see all the travel data and create new travel data
class TravelListView(generics.ListCreateAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# It's the detail view to see, update, or delete a specific travel entry
class TravelDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


# Mixin Class Based Views
# class TravelListView(mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      generics.GenericAPIView):
#     """
#     View to handle GET and POST requests for listing and creating travel data.
#     """
#     queryset = Travel.objects.all()
#     serializer_class = TravelSerializer
#
#     def get(self, request, *args, **kwargs):
#         """
#         List all travel entries.
#         """
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         """
#         Create a new travel entry.
#         """
#         return self.create(request, *args, **kwargs)
#
#
# class TravelDetailView(mixins.RetrieveModelMixin,
#                        mixins.UpdateModelMixin,
#                        mixins.DestroyModelMixin,
#                        generics.GenericAPIView):
#     """
#     View to handle GET, PUT, and DELETE requests for individual travel entries.
#     """
#     queryset = Travel.objects.all()
#     serializer_class = TravelSerializer
#
#     def get(self, request, *args, **kwargs):
#         """
#         Retrieve a travel entry by its ID.
#         """
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         """
#         Update a travel entry by its ID.
#         """
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         """
#         Delete a travel entry by its ID.
#         """
#         return self.destroy(request, *args, **kwargs)

# # Simple  class based views
# class TravelListView(APIView):
#     """
#     View to handle GET requests for listing travel data.
#     """
#     def get(self, request, format=None):
#         """
#         List all travel entries.
#         """
#         snippets = Travel.objects.all()
#         serializer = TravelSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         """
#         Create a new travel entry.
#         """
#         serializer = TravelSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class TravelDetailView(APIView):
#     """
#     View to handle GET requests for listing travel data.
#     """
#     def get_object(self, pk):
#         try:
#             return Travel.objects.get(pk=pk)
#         except Travel.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = TravelSerializer(snippet)
#         return Response(serializer.data)
#
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = TravelSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         """        Delete a travel entry.
#         """
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
#
#
#
#
#         # Logic to retrieve and return travel data
