from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import InterviewPreference, Question

class InterviewAppTests(TestCase):

    def setUp(self):
        self.client = APIClient()

        # Create a user for login and signup tests
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some questions for fetching and generation tests
        self.question1 = Question.objects.create(
            question_text="What is a stack?",
            domain="DSA",
            difficulty="easy",
            interview_type="technical",
            correct_answer="A stack is a LIFO data structure."
        )
        self.question2 = Question.objects.create(
            question_text="Explain polymorphism in OOP.",
            domain="Software Engineering",
            difficulty="medium",
            interview_type="technical",
            correct_answer="Polymorphism is the ability of an object to take on many forms."
        )

    def test_signup(self):
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password': 'newpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)  # One user from setUp and one new user

    def test_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['success'], "Login successful.")

    def test_get_questions(self):
        response = self.client.post(reverse('get_questions'), {
            'domain': 'DSA',
            'difficulty': 'easy',
            'interview_type': 'technical'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['questions']), 1)
        self.assertEqual(response.data['questions'][0]['question_text'], "What is a stack?")

    def test_generate_questions(self):
        response = self.client.post(reverse('generate_questions'), {
            'domain': 'Software Engineering',
            'difficulty': 'medium',
            'interview_type': 'technical'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['questions']), 1)
        self.assertEqual(response.data['questions'][0]['question_text'], "Explain polymorphism in OOP.")
