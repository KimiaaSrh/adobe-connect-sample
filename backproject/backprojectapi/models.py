from django.db import models
from django.contrib.auth.models import User

class Meeting(models.Model):
    title = models.CharField(max_length=80)#8
    description = models.TextField(max_length=300)#2
    url = models.URLField()#11
    category = models.CharField(max_length=50)#3
    startDate = models.DateField()#4
    startTime = models.TextField(max_length=50)#5
    organizer = models.ForeignKey (User, on_delete=models.CASCADE)#6
    # duration=models.DurationField()#7
    passwordOftheMeeting=models.TextField(max_length=50)#9
    extraField=models.TextField(max_length=50)#10
    members=models.TextField(max_length=300)

    def members_list(self):
        allcomments = JoiningtoMeeting.objects.filter(meetingId=self)
        listallcomments = []
        for comment in allcomments:
            print(comment.meetingMember)
            listallcomments.append(comment.meetingMember)
        return listallcomments

    def chats_list(self):
        allcomments =ChatInMeeting.objects.filter(meetingId=self)
        listallcomments = []
        for comment in allcomments:
            print(comment.textBody)
            listallcomments.append(comment.textBody)
        return listallcomments

class Quiz(models.Model):
    duration = models.TextField(max_length=300)
    url = models.URLField()#13
    idOftheQuiz = models.IntegerField()#2 
    quizDesigner = models.ForeignKey (User, on_delete=models.CASCADE)#1
    questions=models.TextField(max_length=300)
    topic=models.CharField(max_length=50)  
    extraField=models.TextField(max_length=50)#12
    startDate = models.DateField()#14
    startTime =models.TextField(max_length=50)#5

    # def questions_list(self):
    #     allcomments = AnsweringQ.objects.filter(quiz=self)
    #     listallcomments = []
    #     for comment in allcomments:
    #         print(comment.questionId)
    #         listallcomments.append(comment.questionId)
    #     return listallcomments

class Question(models.Model):
    # quizNumber=models.ForeignKey (Quiz, on_delete=models.CASCADE,default='')#1
    qNumber=models.IntegerField()
    sooratesoal = models.TextField(max_length=50)
    numberOftheTestAnswers = models.CharField(max_length=50)
    valueOftheTestAnswers = models.TextField(max_length=100)
    trueAnswer=models.TextField(max_length=50)
    typeTest=models.TextField(max_length=50)
    typeEx=models.TextField(max_length=50)
    extraField=models.TextField(max_length=50)#10

class AnsweringQ(models.Model):
    answerOfPerson = models.TextField(max_length=300)
    solver = models.ForeignKey (User, on_delete=models.CASCADE)
    questionId= models.ForeignKey (Question, on_delete=models.CASCADE)
    extraField=models.TextField(max_length=50)#10

    # class Meta:
    #     unique_together = (('solver','questionId'),)
    #     index_together = (('solver','questionId'),)

class JoiningtoMeeting(models.Model):
    meetingMember = models.ForeignKey (User, on_delete=models.CASCADE)
    meetingId= models.ForeignKey (Meeting, on_delete=models.CASCADE)
    extraField=models.TextField(max_length=50)#10

class ChatInMeeting(models.Model):
    writer = models.ForeignKey (User, on_delete=models.CASCADE)
    meetingId= models.ForeignKey (Meeting, on_delete=models.CASCADE)
    textBody=models.TextField(max_length=50)#10
    dateOfSending = models.DateField()#4
    timeOfSending = models.TimeField()#5
    extraField=models.TextField(max_length=50)#10

class QuizQuestion(models.Model):
    question = models.ForeignKey (Question, on_delete=models.CASCADE)
    quiz= models.ForeignKey (Quiz, on_delete=models.CASCADE)