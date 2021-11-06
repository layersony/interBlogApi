from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='home'),
  path('blogs', views.BlogView.as_view()), # Get All Blog
  path('blogPost/', views.BlogPostView.as_view()), # Post A Blog
  path('blogs/<int:pk>', views.BlogDetailView.as_view()), # For Specific blog
  path('auth/register', views.UserRegistrationView.as_view(), name='register'),
  path('auth/login', views.UserLoginView.as_view(), name='login'),
  path('tags/', views.TagView.as_view(), name='tags')
]