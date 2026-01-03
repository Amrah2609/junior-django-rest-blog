from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from favourite.models import Favourite
from favourite.api.serializers import FavouriteListCreateAPISerializer, FavouriteAPISerializer

class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteListCreateAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Favourite.objects.all()
    serializer_class = FavouriteAPISerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
