from django.urls import path
from requests import request

from . import views

urlpatterns = [
    path('',views.Newsfeed_create_api_view), #create newfeed
    path('<int:pk>/',views.Newsfeed_detail_view),
    path('list/',views.Newsfeed_list_view),
    path('<int:pk>/update/',views.Newsfeed_update_view),
    path('<int:pk>/delete/',views.Newsfeed_delete_view),
    path('questions/',views.Question_create_api_view),
    path('questions/list/',views.Questions_list_view),
    path('newsfeed/upvote/',views.upvote),
    path('newsfeed/downvote/',views.downvote),

]