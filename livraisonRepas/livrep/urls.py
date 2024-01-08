from django.urls import path
from .views import *

urlpatterns = [
   
   # Category
   path('createCategorie/', createCategorie, name='createCategorie'),
   path('deleteCategorie/<int:id>/', deleteCategorie, name='deleteCategorie'),
   path('updateCategorie/<int:id>/', updateCategorie, name='updateCategorie'),
   path('listCategorie/', listCategorie, name='listCategorie'),

   # User
   path('create_user/', UserListCreateView.as_view(), name='create_user'),
   path('list_user/', UserAllListView.as_view(), name='list_user'),
   path('delete_user/<int:pk>/', UserDetailView.as_view(), name='delete_user'),
   path('update_user/<int:pk>/', UserUpdate.as_view(), name='update_user'),
   path('is_superuser/', IsSuperuserView.as_view(), name='is_superuser'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('user_profile/',user_profile, name="user_profile"),
   path('get_authenticated_user/', AuthenticatedUserView.as_view(), name='get_authenticated_user'),
   
   # Dishes
   path('list_dishes/', DishesAllListView.as_view(), name='list_dishes'),
   path('delete_recipe/<int:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),
   path('create_dishe/', DisheListCreateView.as_view(), name='create_dishe'),
   path('update_dishe/<int:pk>/', DisheUpdate.as_view(), name='update_dishe'),
   path('search/', search_dishes, name='search_recipes'),

   # Comment
   path('create_comment/', CommentListCreateView.as_view(), name='create_comment'),

   # Favorite
   path('create_favorite/', FavoriteListCreateView.as_view(), name='create_favorite'),
   path('list_ranking/', UserRankingView.as_view(), name='list_ranking'),
   path('list_ranking_with_plat/', RankingWithPlatView.as_view(), name='list_ranking_with_plat'),
   path('check_favorite/<int:user_id>/<int:dish_id>/', check_favorite, name='check_favorite'),
   path('delete_favorite/<int:pk>/', DeleteFavorite.as_view(), name='delete_favorite'),

   # Commande
   path('create_commande/', CommandeListCreateView.as_view(), name='create_commande'),
   path('delete_commande/<int:pk>/', DeleteCommand.as_view(), name='delete_commande'),
   path('list_command_with_plat/', CommandWithPlatView.as_view(), name='list_command_with_plat'),

]