"""social_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Blog.views.postview import PostView
from Users import views as view1
from Blog import views as view2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/authenticate', view1.authenticate_user, name='authenticate-user'),
    path('api/posts', PostView.as_view(), name='get-create-post-api'),
    path('api/posts/<int:post_id>', PostView.as_view(), name='delete-task-api'),
    path('api/all_posts', view2.get_all_posts_api, name="get-all-posts-api"),
    path('api/like/<int:post_id>', view2.like_post_api, name='like-post-api'),
    path('api/unlike/<int:post_id>', view2.unlike_post_api, name='unlike-post-api'),
    path('api/comment/<int:post_id>', view2.comment_on_post, name='comments-post-api')
]
