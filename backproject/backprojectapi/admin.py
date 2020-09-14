from django.contrib import admin

# Register your models here.
from .models import Question, Quiz,AnsweringQ,JoiningtoMeeting,Meeting

admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(AnsweringQ)
admin.site.register(JoiningtoMeeting)
admin.site.register(Meeting)