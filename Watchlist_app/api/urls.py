from django.urls import path
from Watchlist_app.api.views import  watchdetailAPI, streamplatformAPI, streamplatformdetailAPI, reviewlist, reviewdetail, reviewcreate, WatchlistGV

urlpatterns = [
    path('watch/',WatchlistGV.as_view(),name='watch'),
    path('watch/<int:pk>/',watchdetailAPI.as_view(),name='watch'),

    path('stream/',streamplatformAPI.as_view(),name='stream'),
    path('stream/<int:pk>/',streamplatformdetailAPI.as_view(),name='streamdetail'),

    path('watch/<int:pk>/reviewcreate/', reviewcreate.as_view(), name='reviewcreate'),
    path('watch/<int:pk>/review/', reviewlist.as_view(), name='reviewlist'),
    path('watch/review/<int:pk>/',reviewdetail.as_view(),name='review-detail'),
    
    
]