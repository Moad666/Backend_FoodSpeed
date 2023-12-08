from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
    
    

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class PlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plat
        fields = '__all__'

class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'

class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'

class RankingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = '__all__'

class HistoriqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historique
        fields = '__all__'