import spacy
from symptoms.models import Symptom, SymptomRecord

nlp = spacy.load("en_core_web_sm")

def extract_symptoms(text, user=None):
    doc = nlp(text.lower())
    detected = []
    for token in doc:
        if Symptom.objects.filter(name__iexact=token.text).exists():
            symptom = Symptom.objects.get(name__iexact=token.text)
            detected.append(symptom)
            if user:
                SymptomRecord.objects.create(user=user, symptom=symptom)
    return detected
