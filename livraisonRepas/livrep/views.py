from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import *




# Create your views here.

#---------------------------------------------------------Authentification
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()



#---------------------------------------------------------Crud Categorie

@api_view(['POST'])
@permission_classes([AllowAny])
def createCategorie(request):
    if request.method == 'POST':
        serializer = CategorieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def deleteCategorie(request,id):
    try:
        category = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    category.delete()
    return Response({"message": "Category deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([AllowAny])
def listCategorie(request):
    if request.method == 'GET':
        categories = Categorie.objects.all()
        serializer = CategorieSerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([AllowAny])
def updateCategorie(request, id):
    try:
        category = Categorie.objects.get(id=id)
    except Categorie.DoesNotExist:
        return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CategorieSerializer(category, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    
  











