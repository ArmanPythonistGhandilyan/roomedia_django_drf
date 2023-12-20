from django.contrib import admin
from .models import (
    Client,
    SubscribedUser,
    Testimonial,
    FreeConsultation,
    Message,
    LatestPost,
    Expert,
    Comment,
)


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["full_name", "title"]


class FreeConsultationAdmin(admin.ModelAdmin):
    list_display = ["full_name", "phone", "topic"]


class MessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject"]


class LatestPostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_date", "cat"]


class ExpertAdmin(admin.ModelAdmin):
    list_display = ["name", "title"]


class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "date"]


class ClientAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "subscription_type",
        "pricing_package",
        "finish_date",
    ]


admin.site.register(SubscribedUser)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(FreeConsultation, FreeConsultationAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(LatestPost, LatestPostAdmin)
admin.site.register(Expert, ExpertAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Client, ClientAdmin)
