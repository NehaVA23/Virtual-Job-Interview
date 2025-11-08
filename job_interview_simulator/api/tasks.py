# api/tasks.py
from celery import shared_task
import openai

@shared_task
def generate_questions_task(domain, difficulty, interview_type):
    prompt = f"Generate {difficulty} {interview_type} interview questions for {domain}."
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=100,
            n=5,
            stop=None
        )
        questions = [q.strip() for q in response.choices[0].text.split('\n') if q.strip()]
        return questions
    except Exception as e:
        return {"error": str(e)}  