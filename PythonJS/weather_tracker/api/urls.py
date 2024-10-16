from django.urls import path
from api.views import UserView, SearchView
urlpatterns = [
    path('user', UserView.as_view()),
    path('search', SearchView.as_view())
]
