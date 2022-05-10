from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from backend.permissions import IsAuthor, IsAuthorOrReadOnly
from .models import Picture
from .serializers import PictureSerializer

# Create your views here.

class PictureListView(generics.ListCreateAPIView):
    # Permission classes are not applied for list views -> only for views
    # which deal with a single instance of an object.
    permission_classes = (IsAuthenticated, )
    # permission_classes = (IsAuthorOrReadOnly, )
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

class PictureDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Combination of different permission classes to restrict actions on a particular book
    permission_classes = (IsAuthor, )
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
