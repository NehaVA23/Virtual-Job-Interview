from django.contrib import admin
from .models import InterviewPreference, Interview, Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 1  # Number of empty forms to display

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'domain', 'difficulty', 'interview_type')
    list_filter = ('domain', 'difficulty', 'interview_type')
    search_fields = ('question_text', 'domain', 'difficulty')
    inlines = [AnswerInline]  # Adding the inline for answers

# Optional: Register other models as needed
admin.site.register(InterviewPreference)
admin.site.register(Interview)
