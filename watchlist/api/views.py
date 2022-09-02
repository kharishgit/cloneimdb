from rest_framework.response import Response
from watchlist.models import movie
from watchlist.api.serializers import movieSerializer
from rest_framework.decorators import api_view
from rest_framework import status
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method =='GET':
        movies = movie.objects.all()
        serializer = movieSerializer(movies,many=True)
        return Response(serializer.data)
    if request.method =='POST':
        serializer = movieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
@api_view(['GET','PUT','DELETE'])
def movie_index(request,pk):
    if request.method =='GET':
        try:
            movies = movie.objects.get(pk=pk)
        except movie.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = movieSerializer(movies)
        return Response(serializer.data)
    
    if request.method =='PUT':
        movies = movie.objects.get(pk=pk)
        serializer = movieSerializer(movies,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if request.method =='DELETE':
        movies = movie.objects.get(pk=pk)
        movies.delete()
        content ={'Please Move Along with this Movie'}
        return Response(content,status.HTTP_204_NO_CONTENT)


