from django.contrib import admin
from .models import Question,Choice
# Register your models here.

#this is simple costum
'''class QuestionAdmin(admin.ModelAdmin):
    fields=['question_text']'''


class ChoiseInline(admin.StackedInline):
    '''Stacked Inline View for '''

    model = Choice
    extra = 3
    

# here if you have mooore fields in models ,you might want to split the form up into fieldsets:
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ('here we have questions'       ,     {'fields':['question_text']}),
        ('date info',     {'fields':['pub_date'],'classes':['collapse']}),
        
    ]
    inlines=[ChoiseInline]
admin.site.register(Question,QuestionAdmin)

