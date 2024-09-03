from rest_framework import serializers
from Watchlist_app.models import Watchlist, Streamplatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ['watchlist']



class WatchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    platform = serializers.CharField(source='platform.name')
    class Meta:
        model = Watchlist
        fields = "__all__"

    # Object level validation
    def validate(self,data):
        if data['title'] == data['description']:
            raise serializers.ValidationError("Title and description should not be same")
        
        return data


    # Field level validation
    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Name is too short")
        
        return value
    

class StreamplatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)

    class Meta:
        model = Streamplatform
        fields = "__all__"
