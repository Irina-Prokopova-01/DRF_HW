from Ims.apps import ImsConfig
from rest_framework.routers import SimpleRouter
from Ims.views import (
    CourseViewSet,
    LessonCreateAPIView,
    LessonListAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    LessonRetrieveAPIView,
    SubscriptionAPIView,
)
from django.urls import path

app_name = ImsConfig.name

router = SimpleRouter()
router.register("", CourseViewSet)

urlpatterns = [
    path("lesson/create/", LessonCreateAPIView.as_view(), name="lesson_create"),
    path("lesson/", LessonListAPIView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>/", LessonRetrieveAPIView.as_view(), name="lesson_get"),
    path(
        "lesson/update/<int:pk>/", LessonUpdateAPIView.as_view(), name="lesson_update"
    ),
    path(
        "lesson/delete/<int:pk>/", LessonDestroyAPIView.as_view(), name="lesson_delete"
    ),
    path("subscription/", SubscriptionAPIView.as_view(), name="subscription"),
] + router.urls
