from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from .permissions import IsAdminOrReadOnly
from ..models import (
    Comment,
    Expert,
    LatestPost,
    Testimonial,
    Client,
    FreeConsultation,
    Message,
)
from .serializers import (
    ExpertSerializer,
    LatestPostSerializer,
    TestimonialSerializer,
    CommentSerializer,
    ClientSerializer,
    FreeConsultationSerializer,
    MessageSerializer,
)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAdminUser,)


class FreeConsultationViewSet(viewsets.ModelViewSet):
    queryset = FreeConsultation.objects.all()
    serializer_class = FreeConsultationSerializer
    permission_classes = (IsAdminUser,)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAdminUser,)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAdminOrReadOnly,)


class ExpertViewSet(viewsets.ModelViewSet):
    queryset = Expert.objects.all()
    serializer_class = ExpertSerializer
    permission_classes = (IsAdminOrReadOnly,)


class LatestPostViewSet(viewsets.ModelViewSet):
    queryset = LatestPost.objects.all()
    serializer_class = LatestPostSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TestimonialViewSet(viewsets.ModelViewSet):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    permission_classes = (IsAdminOrReadOnly,)
