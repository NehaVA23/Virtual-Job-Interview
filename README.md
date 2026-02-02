# 🎤 Virtual Job Interview Simulator

This project simulates a job interview process with GPT-generated questions, real-time feedback, and voice input support.

## 🔧 Tech Stack

- **Frontend**: React.js, Bootstrap, JavaScript
- **Backend**: Python, Django
- **Database**: MySQL

## 🚀 Features

- Dynamic interview question generation
- Domain and difficulty selection
- Voice and typing input
- AI-generated feedback and grading

## 📁 Folder Structure

- `/job_interview_frontend`: React frontend
- `/job_interview_simulator`: Django backend

## 🛠️ How to Run

### Backend:
```bash
cd job_interview_simulator
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

###Frontend
```bash
cd job_interview_frontend
npm install
npm start
### 4. **(Optional) Add `requirements.txt` for Backend**

In the Django folder (`job_interview_simulator`):

```bash
pip freeze > requirements.txt
This makes it easier to reinstall dependencies late

## 📸 Project Review 

### Domain Selection
![Domain Selection](images/domain-selection.jpg)

### Interview Interface
![Interview](images/interview.jpg)

### Feedback Screen
![Feedback 1](images/feedback-1.jpg)
![Feedback 2](images/feedback-2.jpg)
