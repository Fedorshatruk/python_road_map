from django.contrib import admin

from course.models import OrderRoadMapCourse, RoadMap


class OrderRoadMapInline(admin.StackedInline):
    model = OrderRoadMapCourse
    extra = 0


@admin.register(RoadMap)
class RoadMapAdmin(admin.ModelAdmin):
    inlines = [OrderRoadMapInline]
