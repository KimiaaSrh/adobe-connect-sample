from rest_framework import serializers
from.models import Question, Quiz,AnsweringQ,Meeting,JoiningtoMeeting,ChatInMeeting,QuizQuestion
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class QuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = Question
    fields = '__all__'
    # extra_kwargs = {'url': {'required':True}}

class QuizQuestionSerializer(serializers.ModelSerializer):
  class Meta:
    model = QuizQuestion
    fields = '__all__'


class QuizSerializer(serializers.ModelSerializer):
  class Meta:
    model = Quiz
    fields = '__all__'


class AnsweringQSerializer(serializers.ModelSerializer):
  class Meta:
    model = AnsweringQ
    fields = '__all__'
    # extra_kwargs = {'url': {'required':True}}


class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = '__all__'
    # serialized_obj = serializers.serialize('json', [ , ])
    # fields = ('title','description','url','category','startDate','startTime','organizer','duration','passwordOftheMeeting',
    # 'extraField','members','members_list')

class JoiningtoMeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = JoiningtoMeeting
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id','username','password')
    extra_kwargs = {'password':{'write_only':True,'required':True}}

  def create(self, validated_data):
      user = User.objects.create_user(**validated_data)
      print(user)
      Token.objects.create(user=user)
      return user  

class ChatInMeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = ChatInMeeting
    fields = '__all__'      