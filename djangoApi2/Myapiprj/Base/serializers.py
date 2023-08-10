from rest_framework.serializers import ModelSerializer,SerializerMethodField
from.models import *


class CategorySerializer(ModelSerializer):
    crs_count=SerializerMethodField(read_only=True)
    class Meta:
        model=Category
        fields = "__all__"
        def get_crs_count(self,obj):
            count=obj.course_set.count()
            return count


class CourseSerializer(ModelSerializer):
    class Meta:
        model =Courses
        fields = "__all__"
        Category = CategorySerializer()

