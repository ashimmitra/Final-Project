from django.contrib import admin

from quiz.models import Quiz
from quiz.models import Bangla

class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)

#class BanglaAdmin(admin.ModelAdmin):
    #list_display = ('question',)

admin.site.register(Quiz, QuizAdmin)
#admin.site.register(Bangla, BanglaAdmin)
