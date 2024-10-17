from django.urls import path, include
from app.views import ProfileView, SearchView
urlpatterns = [
    path('profile', ProfileView.as_view()),
    path('search', SearchView.as_view())
]