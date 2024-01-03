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

]