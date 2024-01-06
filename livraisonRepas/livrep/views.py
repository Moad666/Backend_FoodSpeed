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
    authentication_classes = []  # Disable authentication for this view
    permission_classes = []  # Disable permission checks (public access)







