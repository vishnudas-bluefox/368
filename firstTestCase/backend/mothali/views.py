
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from .models import Newsfeed, Questions
from .serializers import NewsfeedSerializer, QuestionSerializer


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
        print(serializer)
        instance = serializer.save()
        if not instance.content:
            instance.content = "No content"

             
        

Newsfeed_update_view = NewsfeedUpdateAPIView.as_view()


# Delete the data from the table
class NewsfeedDestroyAPIView(generics.DestroyAPIView):
    queryset = Newsfeed.objects.all()
    serializer_class = NewsfeedSerializer
    lookup_field = 'pk'

    def perform_update(self, instance):
        super().perform_destroy(instance)
             

Newsfeed_delete_view = NewsfeedDestroyAPIView.as_view()



# create question api_view 
class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
    def perform_create(self, serializer):
        print(serializer.validated_data)
        userid = serializer.validated_data['userid']
        subject=serializer.validated_data['subject']
        description=serializer.validated_data['description']
        answers=serializer.validated_data['answers']
        like=serializer.validated_data['like']
        dislike=serializer.validated_data['dislike']
        serializer.save(userid=userid,subject=subject,description=description,answers=answers,like=like,dislike=dislike)
        #djnago signals
Question_create_api_view = QuestionCreateAPIView.as_view()



# list all questions 
class QuestionsListAPIView(generics.ListAPIView):
    '''
    Not gonna use this
    '''
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer 

Questions_list_view = QuestionsListAPIView.as_view()
# function based view 
@api_view(['PATCH'])
def upvote(request):
    if request.method == 'PATCH':
        data = request.data
        feeddata = Newsfeed.objects.get(pk=request.data['id'])
        feeddata.like = feeddata.like + 1
        feeddata.save()
        return Response({"message": "upvote success"})
    else:
        return Response({"success": False})

@api_view(['PATCH'])
def downvote(request):
    if request.method == 'PATCH':
        data = request.data
        feeddata = Newsfeed.objects.get(pk=request.data['id'])
        feeddata.dislike = feeddata.dislike + 1
        feeddata.save()
        return Response({"message": "downvote success"})
    else:
        return Response({"success": False})


# total 5 five request und 
# GET POST PUT PATCH DELETE
# used requests library to make the request 
# GET POST PATCH DELETE 