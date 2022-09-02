# from django.shortcuts import render
# from watchlist.models import movie
# from django.http import JsonResponse

# # Create your views here.
# def movie_list(request):
#     movies = movie.objects.all()
    
#     data = {
#         'movies' : list(movies.values())
#     }
#     return JsonResponse(data)

# def movie_index(request,pk):
#     movies = movie.objects.get(pk=pk)
#     data = {
#         'name' : movies.name,
#         'description' : movies.description,
#         'active' : movies.active,
#     }
#     return JsonResponse(data)