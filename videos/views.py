from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from .models import Video
from .serializers import VideoSerializer


class VideoList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'
