import joblib
from loguru import logger

svm_model = joblib.load('models/spam_classifier.pkl')
vectorizor = joblib.load('models/vectorizer.pkl')

def get_model():
    return svm_model


def get_vectorization():
    return vectorizor


def info(message:str):
    logger.info(message)

def success(message:str):
    logger.success(message)

def debug(message:str):
    logger.debug(message)

def error(message:str):
    logger.error(message)

def warning(message:str):
    logger.warning(message)