from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Video
from .serializers import VideoSerializer


class VideoList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = '__all__'

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        keyword = self.kwargs['keyword']
        return Video.objects.filter(title__icontains=keyword)


class AbstractVideoView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data={'status': self.status}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class VideoRent(AbstractVideoView):
    status = Video.RENTED


class VideoReturn(AbstractVideoView):
    status = Video.RETURNED
