from django.contrib import admin

from quiz.models import Quiz
from quiz.models import ICT
from quiz.models import Ban
from quiz.models import Ma
from quiz.models import Ban
from quiz.models import Ban

class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)
class ICTAdmin(admin.ModelAdmin):
    list_display = ('question',)
class BanAdmin(admin.ModelAdmin):
    list_display = ('question',)

admin.site.register(Quiz, QuizAdmin)
admin.site.register(ICT, ICTAdmin)
admin.site.register(Ban, BanAdmin)
