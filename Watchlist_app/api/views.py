from Watchlist_app.models import Watchlist, Streamplatform, Review
from Watchlist_app.api.serializers import WatchlistSerializer, StreamplatformSerializer, ReviewSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from Watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from Watchlist_app.api.throttling import ReviewCreateThrottle, ReviewlistThrottle, ReviewdetailThrottle
from Watchlist_app.api.pagination import WatchlistPagination


     # REVIEW CREATE 
class reviewcreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    throttle_classes = [ReviewCreateThrottle]

    def get_queryset(self):
        return Review.objects.all()

    def perform_create(self,serializer):
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)

        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, review_user=review_user)

        if review_queryset.exists():
            raise ValidationError("You have already reviewed")

        serializer.save(watchlist=watchlist, review_user=review_user)





         # REVIEW LIST 
class reviewlist(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    throttle_classes = [ReviewlistThrottle, AnonRateThrottle]
    

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)


       # REVIEW DETAIL 
class reviewdetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [ReviewUserOrReadOnly]
    throttle_classes = [UserRateThrottle, AnonRateThrottle, ReviewdetailThrottle]



   # WATCHLIST CLASS
class WatchlistGV(generics.ListCreateAPIView):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer
    throttle_classes = [AnonRateThrottle]
    pagination_class = WatchlistPagination

        

  # WATCH DETAIL CLASS
class watchdetailAPI(APIView):
    throttle_classes = [AnonRateThrottle]
    def get(self,request,pk):
        watch = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(watch)
        return Response(serializer.data)

    def put(self,request,pk):
        watch = Watchlist.objects.get(pk=pk)
        serializer = WatchlistSerializer(watch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

    def delete(self,request, pk):
        watch = Watchlist.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_200_OK)
    


       # STREAMPLATFORM 
class streamplatformAPI(APIView):
    throttle_classes = [AnonRateThrottle]
    def get(self,request):
        stream = Streamplatform.objects.all()
        serializer = StreamplatformSerializer(stream,many=True)
        return Response(serializer.data)
    

    def post(self,request):
        serializer = StreamplatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


       # STREAM PLATFORM DETAIL 
class streamplatformdetailAPI(APIView):
    throttle_classes = [AnonRateThrottle]
    def get(self,request,pk):
        stream = Streamplatform.objects.get(pk=pk)
        serializer = StreamplatformSerializer(stream)
        return Response(serializer.data)
    

    def put(self,request,pk):
        watch = Streamplatform.objects.get(pk=pk)
        serializer = StreamplatformSerializer(watch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        


    def delete(self,request, pk):
        watch = Streamplatform.objects.get(pk=pk)
        watch.delete()
        return Response(status=status.HTTP_200_OK)



