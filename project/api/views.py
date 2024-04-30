from django.shortcuts import render

# Create your views here.
from api.models import Movie 
from api.serializers import MovieSerializer 
from rest_framework import mixins 
from rest_framework import generics

class MovieList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 
    queryset = Movie.objects.all() 
    serializer_class = MovieSerializer 
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class MovieDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                    generics.GenericAPIView): 
    queryset = Movie.objects.all() 
    serializer_class = MovieSerializer 
    def get(self, request, *args, **kwargs): 
        return self.retrieve(request, *args, **kwargs) 
    def put(self, request, *args, **kwargs): 
        return self.update(request, *args, **kwargs) 
    def delete(self, request, *args, **kwargs): 
        return self.destroy(request, *args, **kwargs)
    
