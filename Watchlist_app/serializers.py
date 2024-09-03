from rest_framework import serializers
from watchlist_app.models import watchlist


class watchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = watchlist
        fields = '__all__'

