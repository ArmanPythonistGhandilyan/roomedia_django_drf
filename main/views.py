import re

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ClientForm, FreeConsultationForm, MessageForm, CommentForm
from .models import Expert, LatestPost, SubscribedUser, Testimonial, Comment


def index(request):
    if request.method == "POST":
        post_data = request.POST.copy()
        email = post_data.get("email", None)
        subscribed_user = SubscribedUser()
        subscribed_user.email = email
        subscribed_user.save()
        # send a confirmation mail
        subject = "NewsLetter Subscription"
        message = (
            "Hello and thanks for subscribing us. "
            "You will get notification of latest articles posted on our "
            "website. Please do not reply on this email."
        )
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [
            email,
        ]
        send_mail(subject, message, email_from, recipient_list)
        res = JsonResponse(
            {"msg": "Thanks. Subscribed Successfully! Check your email."}
        )
        return res

    testimonials = Testimonial.objects.all()
    latest_posts = LatestPost.objects.all()

    return render(
        request,
        "main/index.html",
        context={"testimonials": testimonials, "latest_posts": latest_posts},
    )


def about(request):
    if request.method == "POST":
        form = FreeConsultationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, "main/about.html")

    experts = Expert.objects.all()
    return render(request, "main/about.html", context={"experts": experts})


def contact(request):
    if request.method == "POST":
        form = MessageForm(request.POST or None)
        if form.is_valid():
            print("form is valid")
            form.save()
            return render(request, "main/contact.html")
        else:
            print("Form is not valid")
    return render(request, "main/contact.html")


def blog(request):
    latest_posts = LatestPost.objects.all()

    return render(request, "main/blog.html", context={"latest_posts": latest_posts})


def blog_details(request):
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse("blog_details"))

    latest_posts = LatestPost.objects.all()
    comments = Comment.objects.all()

    return render(
        request,
        "main/blog_details.html",
        context={"latest_posts": latest_posts, "comments": comments},
    )


def portfolio(request):
    return render(request, "main/portfolio.html")


def portfolio_details(request):
    return render(request, "main/portfolio_details.html")


def services(request):
    testimonials = Testimonial.objects.all()

    return render(request, "main/services.html", context={"testimonials": testimonials})


def service_details(request):
    testimonials = Testimonial.objects.all()
    return render(
        request, "main/service_details.html", context={"testimonials": testimonials}
    )


def validate_email(request):
    email = request.POST.get("email", None)
    try:
        is_exists = SubscribedUser.objects.get(email=email)
    except ObjectDoesNotExist:
        is_exists = None
    if email is None:
        res = JsonResponse({"msg": "Email is required."})
    elif is_exists:
        res = JsonResponse({"msg": "Email Address already exists"})
    elif not re.match(r"^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$", email):
        res = JsonResponse({"msg": "Invalid Email Address"})
    else:
        res = JsonResponse({"msg": ""})
    return res


def subscription(request):
    if request.method == "POST":
        form = ClientForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, "main/subscription.html")
    return render(request, "main/subscription.html")
