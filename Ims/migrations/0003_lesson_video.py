# Generated by Django 5.1.4 on 2024-12-29 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Ims", "0002_course_owner_alter_lesson_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="video",
            field=models.URLField(
                blank=True, max_length=255, null=True, verbose_name="Видео"
            ),
        ),
    ]
