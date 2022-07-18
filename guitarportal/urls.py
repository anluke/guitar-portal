from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', views.index),
    path('blog/', views.blog, name='post-list'),
    path('create/', views.post_create, name='post-create'),
    path('post/<id>/', views.post, name='post-detail'),
    path('post/<id>/update/', views.post_update, name='post-update'),
    path('post/<id>/delete/', views.post_delete, name='post-delete'),
    path('tinymce/', include('tinymce.urls')),

]
