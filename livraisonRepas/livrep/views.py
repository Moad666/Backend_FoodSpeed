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
from rest_framework import generics,permissions
from django.contrib.auth.hashers import make_password



# Create your views here.

#---------------------------------------------------------Authentification
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

# check if the user is superUser or not
class IsSuperuserView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        return Response({'is_superuser': user.is_superuser})

# logout
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, *args, **kwargs):
        user_token = Token.objects.get(user=request.user)
        user_token.delete()
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)

#-----------------------------------------------------------------------------------------Crud Categorie

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


#-----------------------------------------------------------------------------------------Crud User
#--------- Create User
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [] 
    permission_classes = []
    def perform_create(self, serializer):
        # Hash the password before saving the user
        hashed_password = make_password(serializer.validated_data.get('password'))
        serializer.validated_data['password'] = hashed_password
        serializer.save()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

#--------- List User
class UserAllListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = []
    permission_classes = []

#--------- Delete User
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [] 
    permission_classes = []
    def perform_update(self, serializer):
        # Hash the password if included in the update data
        password = serializer.validated_data.get('password')
        if password:
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password

        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)


#--------- Update
class UserUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [] 
    permission_classes = []
    def perform_update(self, serializer):
        # Hash the password if included in the update data
        password = serializer.validated_data.get('password')
        if password:
            hashed_password = make_password(password)
            serializer.validated_data['password'] = hashed_password

        serializer.save()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

# User data
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)

class AuthenticatedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user  # Get the authenticated user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#-----------------------------------------------------------------------------------------Crud Dishes
#--------- List Dishes
class DishesAllListView(generics.ListAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    authentication_classes = []
    permission_classes = []

#--------- Delete Dishe
class DeleteRecipe(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    authentication_classes = []  
    permission_classes = []  

#--------- Create Dishe
class DisheListCreateView(generics.ListCreateAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    authentication_classes = [] 
    permission_classes = []

#--------- Update Dishe
class DisheUpdate(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plat.objects.all()
    serializer_class = PlatSerializer
    authentication_classes = [] 
    permission_classes = [] 

#--------- Search
@api_view(['GET'])
@permission_classes([AllowAny])
def search_dishes(request):
    name_query = request.GET.get('name', '')

    if not name_query :
        return Response({"detail": "Please provide a title or categorie for the search."}, status=400)

    queryset = Plat.objects.all()
    queryset = queryset.filter(name__icontains=name_query)

    serializer = PlatSerializer(queryset, many=True)
    return Response(serializer.data)

#-----------------------------------------------------------------------------------------Crud Comment
#--------- Create Comment
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Commentaire.objects.all()
    serializer_class = CommentaireSerializer
    authentication_classes = [] 
    permission_classes = []

#-----------------------------------------------------------------------------------------Crud Favorite
#--------- Create Favorite
class FavoriteListCreateView(generics.ListCreateAPIView):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    authentication_classes = [] 
    permission_classes = []

#--------- List Favorite
class UserRankingView(generics.ListAPIView):
    serializer_class = RankingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Ranking.objects.filter(user=user).order_by('rank')

#--------- Delete Favorite
class DeleteFavorite(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ranking.objects.all()
    serializer_class = RankingSerializer
    authentication_classes = []  
    permission_classes = []


from django.shortcuts import get_object_or_404
from django.http import JsonResponse
#--------- Check
def check_favorite(request, user_id, dish_id):
    user = get_object_or_404(User, id=user_id)
    try:
        favorite = Ranking.objects.get(user=user, plat=dish_id)
        return JsonResponse({'message': 'Dish is a favorite'}, status=200)
    except Ranking.DoesNotExist:
        return JsonResponse({'message': 'Dish is not a favorite'}, status=404)

#--------- Get data from id
class RankingWithPlatView(APIView):
    def get_queryset(self):
        return Ranking.objects.all()

    def get(self, request, *args, **kwargs):
        rankings = self.get_queryset()
        ranking_serializer = RankingSerializer(rankings, many=True)

        data = []

        for ranking_data in ranking_serializer.data:
            plat_id = ranking_data['plat']
            plat = Plat.objects.get(id=plat_id)
            plat_serializer = PlatSerializer(plat)

            ranking_data['plat'] = plat_serializer.data
            data.append(ranking_data)

        return Response(data, status=status.HTTP_200_OK)


#-----------------------------------------------------------------------------------------Crud Commande
#--------- Create Commande
class CommandeListCreateView(generics.ListCreateAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    authentication_classes = [] 
    permission_classes = []

#--------- Delete Command
class DeleteCommand(generics.RetrieveUpdateDestroyAPIView):
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
    authentication_classes = []  
    permission_classes = []  


#--------- Get data from id
class CommandWithPlatView(APIView):
    def get_queryset(self):
        return Commande.objects.all()

    def get(self, request, *args, **kwargs):
        rankings = self.get_queryset()
        ranking_serializer = CommandeSerializer(rankings, many=True)

        data = []

        for ranking_data in ranking_serializer.data:
            plat_id = ranking_data['plat']
            plat = Plat.objects.get(id=plat_id)
            plat_serializer = PlatSerializer(plat)

            ranking_data['plat'] = plat_serializer.data
            data.append(ranking_data)

        return Response(data, status=status.HTTP_200_OK)