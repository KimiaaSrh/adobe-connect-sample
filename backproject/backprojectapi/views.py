from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Quiz, Question,Meeting,JoiningtoMeeting,AnsweringQ,ChatInMeeting,QuizQuestion
from .serializers import QuestionSerializer,QuizSerializer,AnsweringQSerializer,JoiningtoMeetingSerializer,MeetingSerializer,UserSerializer,ChatInMeetingSerializer,QuizQuestionSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token

# Create your views here.
class QuizViewSet(viewsets.ModelViewSet):
  queryset= Quiz.objects.all()
  serializer_class = QuizSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_quiz(self,request,pk=None):
      duration = request.data['duration']
      url = request.data['url']
      idOftheQuiz = request.data['idOftheQuiz']
      questions = request.data['questions']
      topic = request.data['topic']
      startTime = request.data['startTime']
      startDate = request.data['startDate']
      extraField = request.data['extraField']
      quizDesigner=request.user
      rating =Quiz.objects.create(duration=duration,startDate=startDate,startTime=startTime,url=url,extraField=extraField,idOftheQuiz=idOftheQuiz,quizDesigner=quizDesigner,questions=questions,topic=topic)
      serializer = QuizSerializer(rating,many=True)
      response = {'message':'rating created'}
      return Response(response, status=status.HTTP_200_OK)

class QuestionViewSet(viewsets.ModelViewSet):
  queryset= Question.objects.all()
  serializer_class = QuestionSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_question(self,request,pk=None):
      qNumber = request.data['qNumber']
      sooratesoal = request.data['sooratesoal']
      numberOftheTestAnswers = request.data['numberOftheTestAnswers']
      valueOftheTestAnswers = request.data['valueOftheTestAnswers']
      trueAnswer = request.data['trueAnswer']
      typeTest = request.data['typeTest']
      typeEx = request.data['typeEx']
      extraField = request.data['extraField']
      rating =Question.objects.create(qNumber=qNumber,extraField=extraField,sooratesoal=sooratesoal,numberOftheTestAnswers=numberOftheTestAnswers,valueOftheTestAnswers=valueOftheTestAnswers,trueAnswer=trueAnswer,typeEx=typeEx,typeTest=typeTest)
      serializer = QuestionSerializer(rating,many=True)
      response = {'message':'rating created'}
      return Response(response, status=status.HTTP_200_OK)

class AnsweringQViewSet(viewsets.ModelViewSet):
  queryset= AnsweringQ.objects.all()
  serializer_class = AnsweringQSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

class MeetingViewSet(viewsets.ModelViewSet):
  queryset= Meeting.objects.all()
  serializer_class = MeetingSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_meeting(self,request,pk=None):
    # duration=models.DurationField()#7
      title = request.data['title']
      description = request.data['description']
      url = request.data['url']
      category = request.data['category']
      startDate = request.data['startDate']
      startTime = request.data['startTime']
      passwordOftheMeeting = request.data['passwordOftheMeeting']
      extraField = request.data['extraField']
      members = request.data['members']
      organizer = request.user
      # duration=request.data['duration']
      rating =Meeting.objects.create(organizer=organizer,members=members,extraField=extraField,passwordOftheMeeting=passwordOftheMeeting,title=title,description=description,url=url,category=category,startDate=startDate,startTime=startTime)
      serializer = MeetingSerializer(rating,many=True)
      response = {'message':'rating created'}
      return Response(response, status=status.HTTP_200_OK)


class JoiningtoMeetingViewSet(viewsets.ModelViewSet):
  queryset= JoiningtoMeeting.objects.all()
  serializer_class = JoiningtoMeetingSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  @action(methods=['POST'], detail=True)
  def create_joinToMeeting(self,request,pk=None):
      meetingMember = request.user
      meetingId = Meeting.objects.get(id=pk)
      extraField = request.data['extraField']
      rating =JoiningtoMeeting.objects.create(extraField=extraField,meetingId=meetingId,meetingMember=meetingMember)
      serializer = JoiningtoMeetingSerializer(rating,many=True)
      response = {'message':'rating created'}
      return Response(response, status=status.HTTP_200_OK)

class QuizQuestionViewSet(viewsets.ModelViewSet):
  queryset= QuizQuestion.objects.all()
  serializer_class = QuizQuestionSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

  # @action(methods=['POST'], detail=True)
  # def create_quizquestion(self,request,pk=None):
  #     quiz=Quiz.objects.last()
  #     question=Question.objects.last()
  #     rating =QuizQuestion.objects.create(quiz=quiz,question=question)
  #     serializer = QuizQuestionSerializer(rating,many=True)
  #     response = {'message':'rating created'}
  #     return Response(response, status=status.HTTP_200_OK)


class ChatInMeetingViewSet(viewsets.ModelViewSet):
  queryset= ChatInMeeting.objects.all()
  serializer_class = ChatInMeetingSerializer
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = (AllowAny, )
  

  # @action(methods=['POST'], detail=True)
  # def create_user(self,request,pk=None):
  #     username = request.data['username']
  #     password = request.data['password']
  #     user = User.objects.create(username=user,password=password)
  #     # print(user)
  #     Token.objects.create(user=user)
  #     return user