from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, NoteViewSet


router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('notes',NoteViewSet)

urlpatterns = [
    path('', include(router.urls)),
]