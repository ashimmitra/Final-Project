from django.contrib import admin

from quiz.models import Quiz
from quiz.models import Bangla
from quiz.models import Math
from quiz.models import Science
from quiz.models import GK
from quiz.models import GNK
from quiz.models import Sci
from quiz.models import Mat
from quiz.models import ICT
from quiz.models import Ban

class QuizAdmin(admin.ModelAdmin):
	list_display = ('question',)
class BanglaAdmin(admin.ModelAdmin):
    list_display = ('question',)
class MathAdmin(admin.ModelAdmin):
    list_display = ('question',)
class ScienceAdmin(admin.ModelAdmin):
    list_display = ('question',)
class GKAdmin(admin.ModelAdmin):
    list_display = ('question',)
class GNKAdmin(admin.ModelAdmin):
    list_display = ('question',)
class MatAdmin(admin.ModelAdmin):
    list_display = ('question',)
class SciAdmin(admin.ModelAdmin):
    list_display = ('question',)
class ICTAdmin(admin.ModelAdmin):
    list_display = ('question',)
#class BanAdmin(admin.ModelAdmin):
    #list_display = ('question',)                 

admin.site.register(Quiz, QuizAdmin)
admin.site.register(Bangla, BanglaAdmin)
admin.site.register(Math, MathAdmin)
admin.site.register(Science, ScienceAdmin)
admin.site.register(GK, GKAdmin)
admin.site.register(ICT, ICTAdmin)
#admin.site.register(Ban, BanAdmin)
admin.site.register(Mat, MatAdmin)
admin.site.register(Sci, SciAdmin)
admin.site.register(GNK, GNKAdmin)