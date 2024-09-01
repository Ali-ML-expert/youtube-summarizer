from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('single-video-summary/', views.single_video_summary, name='single_video_summary'),
    path('search/', views.search, name='search'),
    path('search/results/<str:query>/', views.search_results, name='search_results'),
    path('history/', views.history, name='history'),
    path('profile/', views.user_profile, name='user_profile'),
    path('login/', auth_views.LoginView.as_view(template_name='summarizer/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
