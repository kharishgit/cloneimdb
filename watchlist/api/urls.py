from django.urls import path
from watchlist.api import views


urlpatterns =[
    path('list/',views.movie_list,name='movie_list'),
    path('list/<int:pk>',views.movie_index, name='movie_index'),
]