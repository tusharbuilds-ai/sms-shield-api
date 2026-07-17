import joblib

svm_model = joblib.load('models/spam_classifier.pkl')
vectorizor = joblib.load('models/vectorizer.pkl')

def get_model():
    return svm_model


def get_vectorization():
    return vectorizor