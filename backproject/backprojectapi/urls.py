from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import QuestionViewSet,QuizViewSet, AnsweringQViewSet,JoiningtoMeetingViewSet,MeetingViewSet,UserViewSet,QuizQuestionViewSet


router=routers.DefaultRouter()
router.register('meeting',MeetingViewSet)
router.register('question',QuestionViewSet)
router.register('quiz',QuizViewSet)
router.register('answering',AnsweringQViewSet)
router.register('join',JoiningtoMeetingViewSet)
router.register('users',UserViewSet)
router.register('qq',QuizQuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]