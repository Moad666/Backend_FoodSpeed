from django.urls import path
from .views import *

urlpatterns = [
   path('createCategorie/', createCategorie, name='createCategorie'),
   path('deleteCategorie/<int:id>/', deleteCategorie, name='deleteCategorie'),
   path('updateCategorie/<int:id>/', updateCategorie, name='updateCategorie'),
   path('listCategorie/', listCategorie, name='listCategorie'),

]