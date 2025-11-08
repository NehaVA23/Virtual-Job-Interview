from django.db import models
from django.utils import timezone


class InterviewPreference(models.Model):
    domain = models.CharField(max_length=100)  # Domain of the interview
    difficulty = models.CharField(max_length=10, choices=[
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ], default='medium')  # Set a default value for difficulty
    interview_type = models.CharField(max_length=20)  # Type of interview (e.g., HR, technical)

    def __str__(self):
        return f"{self.domain} - {self.difficulty} - {self.interview_type}"

class Interview(models.Model):
    preference = models.ForeignKey(InterviewPreference, on_delete=models.CASCADE)  # Link to InterviewPreference
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of when the interview was created

    def __str__(self):
        return f"{self.preference.domain} - {self.preference.difficulty} - {self.preference.interview_type}"

class Question(models.Model):
    DOMAIN_CHOICES = [
        ('DSA', 'Data Structures'),
        ('Software Engineering', 'Software Engineering'),
        ('Web Development', 'Web Development'),
        # Add more domains as necessary
    ]

    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    INTERVIEW_TYPE_CHOICES = [
        ('HR', 'HR'),
        ('technical', 'Technical'),
        ('managerial', 'Managerial'),
    ]

    question_text = models.CharField(max_length=500)  # The actual question text
    domain = models.CharField(max_length=50, choices=DOMAIN_CHOICES)  # Domain of the question
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='medium')  # Set a default value for difficulty
    interview_type = models.CharField(max_length=50, choices=INTERVIEW_TYPE_CHOICES)  # Type of interview
    correct_answer = models.CharField(max_length=255, blank=True, null=True)  # The correct answer

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # Link to Question model
    user_answer = models.TextField()  # The answer provided by the user
    correct_answer = models.TextField()  # The correct answer for validation
    is_correct = models.BooleanField(default=False)  # Indicates if the user's answer is correct
    created_at = models.DateTimeField(default=timezone.now)  # Timestamp for answer submission

    def __str__(self):
        return f"Answer for '{self.question.question_text}': '{self.user_answer}' (Correct: {self.is_correct})"
