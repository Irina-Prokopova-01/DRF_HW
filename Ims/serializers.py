from rest_framework.serializers import ModelSerializer, SerializerMethodField

from Ims.models import Course, Lesson


class CourseSerializer(ModelSerializer):
    """Сериализатор курса."""

    lessons_total = SerializerMethodField()
    lessons = SerializerMethodField()

    def get_lessons(self, course):
        """Выводим информацию по урокам"""
        return [
            f"{lesson.title} - {lesson.description}"
            for lesson in course.lesson_set.all()
        ]

    def get_lessons_total(self, course):
        """Получаем всего уроков в курсе."""
        return course.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'

class LessonSerializer(ModelSerializer):
    """Сериализатор урока."""

    course = CourseSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = "__all__"






