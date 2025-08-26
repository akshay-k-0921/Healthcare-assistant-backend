from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

DEFAULT_CONTEXT = """
I am a healthcare assistant. I can provide information about common symptoms,
basic first aid, general health advice, and over-the-counter medication guidance.
I do not replace professional medical advice.
"""

from .symptom_extractor import extract_symptoms
from symptoms.models import DoctorSuggestion

def get_ai_response(user_input, user=None):
    # Extract symptoms
    symptoms = extract_symptoms(user_input, user=user)
    symptoms_names = [s.name for s in symptoms]

    # Doctor suggestions
    doctors = []
    for s in symptoms:
        suggestions = DoctorSuggestion.objects.filter(symptom=s)
        doctors += [d.doctor_specialty for d in suggestions]

    # AI chatbot answer
    try:
        result = qa_pipeline({
            "question": user_input,
            "context": DEFAULT_CONTEXT
        })
        answer = result.get("answer", "").strip()
        if len(answer) < 3:
            answer = "I’m not sure about that. Could you provide more details?"

    except:
        answer = "Sorry, I am having trouble understanding right now. Please try again."

    response = answer
    if symptoms_names:
        response += f" Detected symptoms: {', '.join(symptoms_names)}."
    if doctors:
        response += f" Recommended doctor specialties: {', '.join(set(doctors))}."

    return response
