from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions
from app_classviews.serializers import TravelSerializer
from app_classviews.permissions import IsOwnerOrReadOnly
from rest_framework import viewsets
from django.contrib.auth.models import User
from app_classviews.serializers import UserSerializer
from app_classviews.models import Travel
from rest_framework import renderers


# Create your views here.
# view_sets
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This view_set automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CricketViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        """
        This method allows us to highlight a travel instance.
        """
        travel = self.get_object()
        return Response(travel.highlighted)

    def perform_create(self, serializer):
        """
        This method allows us to set the owner of the travel instance
        to the current user.
        """
        serializer.save(owner=self.request.user)
