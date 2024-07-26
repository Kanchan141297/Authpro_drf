from rest_framework import viewsets
from .serializer import BlogSerializer
from blog_app.models import Blog
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BlogViewsetAPI(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    authentication_classes =[TokenAuthentication]
    permission_classes =[IsAuthenticated]