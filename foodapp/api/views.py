from rest_framework.decorators import api_view , APIView
from rest_framework.response import Response
from .serializers import *
from foodapp.models import *
from django.contrib.postgres.search import SearchVector, SearchRank ,SearchQuery
from django.db.models import Q
import json
from rest_framework.generics import ListAPIView , RetrieveAPIView ,CreateAPIView

#### Basic ORM Filtering ######
class All_Recipes(APIView):
    def get(self,request):
        q = request.GET.get('tags')
        if q:
            q_list = json.loads(q)
            search_queries = [item["value"] for item in q_list]

        recipes = Recipe.objects.only('ingredient__ingredient_name__name')\
                                .prefetch_related('ingredient').\
                                filter(ingredient__ingredient_name__name__in=search_queries).distinct('id')
  
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

### Full Text Search ###
class All_Recipes2(APIView):
    def get(self,request):
        q = request.GET.get('tags')



class GetBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class GetSingleBlog(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CreateMessage(CreateAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer


# class GalleryImages(ListAPIView):
#     queryset = 
#     serializer_class = 