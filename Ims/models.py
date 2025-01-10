from django.db import models


class Course(models.Model):
    """Модель курса"""

    title = models.CharField(
        max_length=150, verbose_name="Название", help_text="Введите название курса"
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание категории",
    )
    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        blank=True,
        null=True,
        help_text="Загрузите фотографию курса",
    )
    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владелец курса",
        on_delete=models.SET_NULL,
        help_text="Введите владельца курса",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Lesson(models.Model):
    """Модель урока"""

    title = models.CharField(
        max_length=300,
        verbose_name="Название урока",
        help_text="Введите название урока",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание урока",
    )
    preview = models.ImageField(
        upload_to="Ims/previews",
        verbose_name="Превью",
        blank=True,
        null=True,
        help_text="Загрузите изображение",
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс",
        help_text="Выберите курс",
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        "users.User",
        verbose_name="Владелец урока",
        on_delete=models.SET_NULL,
        help_text="Введите владельца урока",
        null=True,
        blank=True,
    )
    video = models.URLField(max_length=255, blank=True, null=True, verbose_name="Видео")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Subscription(models.Model):
    """Модель подписки"""

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, verbose_name="пользователь"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    def __str__(self):
        return f"Вы {self.user} подписаны на курс #{self.course}"

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
