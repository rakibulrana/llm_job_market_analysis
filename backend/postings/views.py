from rest_framework import viewsets

from .models import Posting
from .serializers import PostingSerializer


class PostingViewSet(viewsets.ModelViewSet):
    queryset = Posting.objects.all()
    serializer_class = PostingSerializer
