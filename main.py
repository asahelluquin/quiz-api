##CODIGO API

from fastapi import FastAPI
from pydantic import BaseModel
from quiz_generator import generate_quiz

app = FastAPI()

class QuizRequest(BaseModel):
    text: str
    num_questions: int = 3

@app.get("/")
def root():
    return {"message": "Quiz API funcionando"}

@app.post("/generate-quiz")
def create_quiz(request: QuizRequest):
    quiz = generate_quiz(request.text, request.num_questions)
    
    return {
        "quiz": quiz
    }