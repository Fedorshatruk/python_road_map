from django.db.models import Prefetch
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView

from course.models import RoadMap, OrderRoadMapCourse, Course, Lesson


class RoadMapView(ListView):
    template_name = 'course/road_map_list.html'
    model = RoadMap

    def get(self, request, *args, **kwargs):
        if self.get_queryset().count() == 1:
            return redirect(reverse('course:road_map_detail', kwargs={'pk': self.get_queryset().first().pk}))
        return super().get(request, *args, **kwargs)


class RoadMapDetail(DetailView):
    template_name = 'course/road_mad_detail.html'
    model = RoadMap

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.prefetch_related(
            Prefetch(
                'order_course',
                queryset=OrderRoadMapCourse.objects.select_related('course').order_by('order_num')
            )
        )


class CourseDetailView(DetailView):
    template_name = 'course/course_detail.html'
    model = Course

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            Prefetch(
                'lessons',
                queryset=Lesson.objects.prefetch_related('links')
            )
        )
