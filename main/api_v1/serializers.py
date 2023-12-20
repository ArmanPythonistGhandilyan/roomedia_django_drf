from rest_framework import serializers
from ..models import (
    Comment,
    Expert,
    LatestPost,
    Testimonial,
    Client,
    FreeConsultation,
    Message,
)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class FreeConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FreeConsultation
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = "__all__"


class LatestPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = LatestPost
        fields = "__all__"


class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"
