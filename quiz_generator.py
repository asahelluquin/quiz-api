'''from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")
'''
def generate_quiz(text, num_questions=3):
    quiz = []
    
    for i in range(num_questions):
        quiz.append({
            "question": f"¿Pregunta {i+1} sobre el texto?",
            "options": ["A", "B", "C", "D"],
            "answer": "A"
        })
    
    return quiz