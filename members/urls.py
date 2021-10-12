
from django.urls import path,include
from . import views
from .views import UserRegisterView,PasswordsChangeView,UserEditProfileView,ShowProfileView,settingsview,CreateProfileView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/',UserRegisterView.as_view(),name = 'register'),
    path('profile/',views.get_user_profile,name = 'profile'),
    path('<int:pk>/profile/',ShowProfileView.as_view(),name = 'user_profile'),
    path('create_profile/',CreateProfileView.as_view(),name = 'create_profile'),
    path('<int:pk>/edit_profile/',UserEditProfileView.as_view(),name = 'edit_profile'),
    #path('password/',auth_views.PasswordChangeView.as_view(template_name = 'registration/change-password.html'))
    path('<int:pk>/settings/',settingsview.as_view(),name = 'settings'),
    path('password/',PasswordsChangeView.as_view(template_name = 'registration/change-password.html'))
    
]
