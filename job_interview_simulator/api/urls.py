from django.urls import path
from .views import (
    InterviewPreferenceCreate,
    GetQuestionsView,
    GenerateAIQuestionView,
    FeedbackView,
    GetCorrectAnswerView,
    SignupView,
    LoginView,
    home,
)

urlpatterns = [
    path('', home, name='home'),  # Home route
    path('interview-preference/', InterviewPreferenceCreate.as_view(), name='interview_preference_create'),  # Create interview preferences
    path('get-questions/', GetQuestionsView.as_view(), name='get_questions'),  # Fetch questions based on preferences
    path('generate-questions/', GenerateAIQuestionView.as_view(), name='generate_questions'),  # Generate AI questions
    path('feedback/', FeedbackView.as_view(), name='feedback'),  # Get feedback on answers
    path('get-correct-answer/', GetCorrectAnswerView.as_view(), name='get_correct_answer'),
    path('signup/', SignupView.as_view(), name='signup'),  # User signup
    path('login/', LoginView.as_view(), name='login'),  # User login
]
