from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from users.views import UserAPIView, RegisterAPIView
from posts.views import PostAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserAPIView.as_view()),
    path('users/register/', RegisterAPIView.as_view()),
    path('posts/', PostAPIView.as_view()),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)