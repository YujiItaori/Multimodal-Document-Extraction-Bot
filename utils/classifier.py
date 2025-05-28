# classifier.py improvements
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
import joblib
import os

MODEL_PATH = "models/classifier.pkl"
VECTORIZER_PATH = "models/vectorizer.pkl"

# Sample training data (should be expanded)
TRAINING_DATA = [
    ("invoice", "This is an invoice for services rendered"),
    ("invoice", "Invoice number 12345 date 01/01/2023"),
    ("resume", "John Doe Curriculum Vitae Work Experience"),
    ("resume", "Resume of Jane Smith Education Background"),
    ("id", "Government of Example Passport Number"),
    ("id", "Driver License ID 12345678")
]

def train_classifier():
    texts = [text for _, text in TRAINING_DATA]
    labels = [label for label, _ in TRAINING_DATA]
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(texts)
    
    classifier = LinearSVC()
    classifier.fit(X, labels)
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(classifier, MODEL_PATH)
    joblib.dump(vectorizer, VECTORIZER_PATH)

def classify_document(text):
    if not os.path.exists(MODEL_PATH):
        train_classifier()
    
    classifier = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    
    features = vectorizer.transform([text])
    return classifier.predict(features)[0].capitalize()