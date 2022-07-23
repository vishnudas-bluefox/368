
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Newsfeed
from .serializers import NewsfeedSerializer


# Create your views here.
#generic view
# for create the news feeds 
class NewsfeedCreateAPIView(generics.CreateAPIView):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    def perform_create(self, serializer):
        print(serializer.validated_data)
        userid = serializer.validated_data['userid']
        title=serializer.validated_data['title']
        content=serializer.validated_data['content']
        media=serializer.validated_data['media']
        like=serializer.validated_data['like']
        dislike=serializer.validated_data['dislike']
        comments=serializer.validated_data['comments']

        
        if content is None:
            content="No content"
        serializer.save(userid=userid,title=title,content=content,media=media,like=like,dislike=dislike,comments=comments)
        #djnago signals
Newsfeed_create_api_view = NewsfeedCreateAPIView.as_view()


# retrive single data from the tables datas in the table 

class NewsfeedDetailAPIView(generics.RetrieveAPIView):
    queryset = Newsfeed.objects.all()
    print(queryset)
    serializer_class = NewsfeedSerializer
    lookup_field = 'pk'

Newsfeed_detail_view = NewsfeedDetailAPIView.as_view()


# list all the data in the tables 

class NewsfeedListAPIView(generics.ListAPIView):
    '''
    Not gonna use this
    '''
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer 

Newsfeed_list_view = NewsfeedListAPIView.as_view()



# update everything with feed  

class NewsfeedUpdateAPIView(generics.UpdateAPIView):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = "No content"

             
        

Newsfeed_update_view = NewsfeedUpdateAPIView.as_view()
