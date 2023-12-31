# Generated by Django 4.2.7 on 2023-12-04 07:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_alter_latestpost_cat_alter_testimonial_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="latestpost",
            name="cat",
            field=models.CharField(
                choices=[
                    (".filterNews", "News"),
                    (".filterBusiness", "Business"),
                    (".filterTechnology", "Technology"),
                    (".filterCommunity", "Community"),
                    (".filterEvents", "Events"),
                    (".filterOthers", "Other"),
                ],
                max_length=20,
                verbose_name="Category filter",
            ),
        ),
    ]
