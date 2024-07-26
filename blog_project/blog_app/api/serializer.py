from rest_framework import serializers
from blog_app.models import Blog


class BlogSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format="%d/%m/%Y %H:%M",read_only=True)

    class Meta:
        model = Blog
        fields = "__all__"