from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

def generate_quiz(text, num_questions=3):
    prompt = f"generate {num_questions} questions with answers: {text}"
    
    result = generator(prompt, max_length=200, do_sample=True)
    
    output = result[0]['generated_text']
    
    # Formato simple (puedes mejorar luego)
    questions = output.split("?")
    
    quiz = []
    
    for q in questions[:num_questions]:
        if len(q.strip()) > 10:
            quiz.append({
                "question": q.strip() + "?",
                "options": ["Opción A", "Opción B", "Opción C", "Opción D"],
                "answer": "Opción A"
            })
    
    return quiz