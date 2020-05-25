from django.urls import include, path

from news.views import PostListCreateList, CommentCreateList, PostDetail

api_urlpatterns = [
    path('news/', PostListCreateList.as_view(), name="news"),
    path('news/<int:pk>', PostDetail.as_view(), name='news-detail'),
    path('comments/', CommentCreateList.as_view(), name="comment"),
]

urlpatterns = [
    path('api/', include(api_urlpatterns))
]
