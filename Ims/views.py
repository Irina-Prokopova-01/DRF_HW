from rest_framework import viewsets, generics
from users.permissions import IsOwner, IsModerator
from Ims.serializers import CourseSerializer, LessonSerializer
from Ims.models import Course, Lesson
from rest_framework.permissions import IsAuthenticated



class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def perform_create(self, serializer):
        """Обьект владельца = текущий пользователь"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()

    def get_permissions(self):
        if self.action == 'create':
            self.permission_classes = [~IsModerator]
        elif self.action in ["retrieve", "update"]:
            self.permission_classes = (IsModerator | IsOwner,)
        elif self.action == 'destroy':
            self.permission_classes = (~IsModerator | IsOwner,)
        return super().get_permissions()


class LessonCreateAPIView(generics.CreateAPIView):
    """Реализация представления создания уроков через generic. CreateAPIView"""
    serializer_class = LessonSerializer
    permission_classes = (~IsModerator, IsAuthenticated)

    def perform_create(self, serializer):
        """Обьект владельца = текущий пользователь"""
        course = serializer.save()
        course.owner = self.request.user
        course.save()


class LessonListAPIView(generics.ListAPIView):
    """Реализация представления просмотра всех уроков через generic. ListAPIView"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Реализация представления просмотра одного урока через generic. ListAPIView"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Реализация представления изменения урока через generic. UpdateAPIView"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    permission_classes = (IsAuthenticated, IsModerator | IsOwner,)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Реализация представления удаления урока через generic. DestroyAPIView"""
    queryset = Lesson.objects.all()

    permission_classes = (IsAuthenticated, ~IsModerator | IsOwner,)