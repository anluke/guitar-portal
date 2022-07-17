from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('blog/', views.blog, name='post-list'),
    path('post/<id>/', views.post, name='post-detail'),
    path('tinymce/', include('tinymce.urls')),

]
