from django.urls import path
from . import views

urlpatterns = [
    path('movies/', views.MovieCreateListeView.as_view(), name='movie-create-list'),
    path('movies/<int:pk>',views.MovieRetrieveUpdateDestroy.as_view(),name='movie-detail-view'),
    path('movies/stats/',views.MovieStatsView.as_view(),name='moview-stats-view'),
]