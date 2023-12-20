from django import forms
from .models import Client, FreeConsultation, Message, Comment


class FreeConsultationForm(forms.ModelForm):
    class Meta:
        model = FreeConsultation
        fields = ["full_name", "phone", "topic", "message"]


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["name", "email", "subject", "message"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "email", "website", "comment"]


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            "name",
            "email",
            "subscription_type",
            "pricing_package",
            "card_number",
            "expiration_date",
            "cvv",
            "finish_date",
        ]
