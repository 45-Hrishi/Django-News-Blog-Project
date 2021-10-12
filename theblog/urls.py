from django.urls import path
from . import views


urlpatterns = [
    path('',views.HomeView.as_view(),name = 'home'),
    path('article/<int:pk>/',views.ArticleDetailView.as_view(),name = 'article-detail'),
    path('new_post/',views.AddPostView.as_view(),name = 'new_post'),
    path('new_category/',views.AddCategoryView.as_view(),name = 'new_category'),
    path('article/edit/<int:pk>/',views.UpdatePostView.as_view(),name = 'update_post'),
    path('article/<int:pk>/delete/',views.DeletePostView.as_view(),name = 'delete'),
    path('category/<str:cats>/',views.CategoryView,name = 'category'),
    path('like/<int:pk>/',views.LikeView,name = 'like_post'),
    path('post/<int:pk>/likes/',views.post_likes,name = 'likes'),
    path('article/<int:pk>/add_comment/',views.AddCommentView.as_view(),name = "add_comment"),
    path('profile/My_posts/',views.userposts,name = 'userposts'),
    
]