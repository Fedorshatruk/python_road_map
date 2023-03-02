from django.contrib import admin
from django.db.models import F

from course.models import Lesson


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'course_name',
        'order_num',
    )
    list_filter = (
        'course',
    )

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(course_name=F('course__name'))

    @admin.display(ordering='course__name', description='курс')
    def course_name(self, obj):
        return obj.course_name