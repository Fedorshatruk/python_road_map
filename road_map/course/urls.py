from django.urls import path

from course.apps import CourseConfig
from course.views import RoadMapView, RoadMapDetail, CourseDetailView

app_name = CourseConfig.name

urlpatterns = [
    path('', RoadMapView.as_view(), name='road_map_list'),
    path('<int:pk>/', RoadMapDetail.as_view(), name='road_map_detail'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
]
