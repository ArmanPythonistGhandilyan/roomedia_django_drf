from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("blog/", views.blog, name="blog"),
    path("blog_details/", views.blog_details, name="blog_details"),
    path("portfolio/", views.portfolio, name="portfolio"),
    path("portfolio_details/", views.portfolio_details, name="portfolio_details"),
    path("services/", views.services, name="services"),
    path("service_details/", views.service_details, name="service_details"),
    path("validate/", views.validate_email, name="validate_email"),
    path("subscription/", views.subscription, name="subscription"),
    path("api/v1/", include("main.api_v1.urls")),
]
