from django.contrib import admin

from quiz.models import Quiz
from quiz.models import ICT
from quiz.models import Ban
from quiz.models import Math
from quiz.models import Science
from quiz.models import GK

class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)
class ICTAdmin(admin.ModelAdmin):
    list_display = ('question',)
class BanAdmin(admin.ModelAdmin):
    list_display = ('question',)
class MathAdmin(admin.ModelAdmin):
    list_display = ('question',)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('question',)
class GkAdmin(admin.ModelAdmin):
    list_display = ('question',)    

admin.site.register(Quiz, QuizAdmin)
admin.site.register(ICT, ICTAdmin)
admin.site.register(Ban, BanAdmin)
admin.site.register(, MathAdmin)
admin.site.register(Ban, BanAdmin)
admin.site.register(Ban, BanAdmin)
