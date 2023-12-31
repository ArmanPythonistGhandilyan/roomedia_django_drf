# Generated by Django 4.2.7 on 2023-12-08 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0007_alter_comment_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="img",
            field=models.ImageField(
                default="assets/img/anonymous_user_img.jpg",
                upload_to="images",
                verbose_name="User's image",
            ),
        ),
    ]
