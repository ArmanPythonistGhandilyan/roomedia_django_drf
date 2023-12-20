from datetime import date, timedelta
from django.db import models


class SubscribedUser(models.Model):
    email = models.EmailField("User email", unique=True, max_length=30)

    def __str__(self):
        return self.email

    objects = models.Manager()


class Testimonial(models.Model):
    full_name = models.CharField("Full name", max_length=30)
    title = models.CharField("Title", max_length=50)
    text = models.TextField("Text")
    img = models.ImageField("Image", upload_to="images", null=True, blank=True)

    def __str__(self):
        return self.full_name

    objects = models.Manager()


class FreeConsultation(models.Model):
    full_name = models.CharField("Full name", max_length=30)
    phone = models.CharField("Phone", max_length=20)
    topic = models.CharField("Topic", max_length=10)
    message = models.TextField("Message")

    def __str__(self):
        return self.full_name

    objects = models.Manager()


class Message(models.Model):
    name = models.CharField("Name", max_length=30)
    email = models.EmailField("Email", unique=True)
    subject = models.CharField("Optional subject", max_length=30, blank=True)
    message = models.TextField("Message")

    def __str__(self):
        return self.email

    objects = models.Manager()


class LatestPost(models.Model):
    categories = [
        ("filterNews", "News"),
        ("filterBusiness", "Business"),
        ("filterTechnology", "Technology"),
        ("filterCommunity", "Community"),
        ("filterEvents", "Events"),
        ("filterOthers", "Other"),
    ]

    img = models.ImageField("Post image", upload_to="images")
    title = models.CharField("Post title", max_length=30)
    content = models.CharField("Post content", max_length=50)
    created_date = models.DateField("Post's created date", auto_now=True)
    cat = models.CharField("Category filter", max_length=20, choices=categories)

    def __str__(self):
        return self.title

    objects = models.Manager()


class Expert(models.Model):
    img = models.ImageField("Image", upload_to="images")
    name = models.CharField("Name", max_length=30)
    title = models.CharField("Title", max_length=50)

    def __str__(self):
        return self.name

    objects = models.Manager()


class Comment(models.Model):
    name = models.CharField("Name", max_length=30)
    email = models.EmailField("Email")
    website = models.CharField("Website", max_length=30, null=True)
    comment = models.CharField("Comment", max_length=255)
    date = models.DateTimeField("Published date", auto_now_add=True)
    img = models.ImageField(
        "User's image", default="images/anonymous_user_img.png", upload_to="images"
    )

    def __str__(self):
        return self.name

    objects = models.Manager()


class Client(models.Model):
    name = models.CharField("Name", max_length=30)
    email = models.EmailField("Email", unique=True)
    subscription_type = models.CharField("Subscription type", max_length=10)
    pricing_package = models.CharField("Pricing package", max_length=20)
    card_number = models.CharField("Card number", max_length=16)
    expiration_date = models.CharField("Expiration date", max_length=5)
    cvv = models.IntegerField("CVV")
    start_date = models.DateField("Start date")
    finish_date = models.DateField("Finish date", blank=True)

    def save(self, *args, **kwargs):
        self.start_date = date.today()

        if self.subscription_type == "monthly":
            delta = timedelta(days=30)
        elif self.subscription_type == "annual":
            delta = timedelta(days=365)

        self.finish_date = self.start_date + delta

        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    objects = models.Manager()
