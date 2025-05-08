from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InternViewSet, TaskViewSet, AbsenceViewSet

router = DefaultRouter()
router.register(r'interns', InternViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'absences', AbsenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 