import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.impute import SimpleImputer
import joblib

# Definir diccionarios de mapeo para las categorías
gender_mapping = {'Male': 0, 'Female': 1}
occupation_mapping = {'Engineer': 0, 'Teacher': 1, 'Student': 2, 'Manager': 3, 'Accountant': 4,
                      'Nurse': 5, 'Lawyer': 6, 'Artist': 7, 'IT': 8, 'Doctor': 9,
                      'Consultant': 10, 'Analyst': 11, 'Salesman': 12, 'Marketing': 13,
                      'Architect': 14, 'Designer': 15, 'Pharmacist': 16, 'Researcher': 17,
                      'Professor': 18, 'Pilot': 19, 'Receptionist': 20, 'Banker': 21,
                      'Writer': 22, 'Chef': 23, 'Veterinarian': 24, 'Sales': 25,
                      'HR': 26, 'Electrician': 27, 'Musician': 28, 'Programmer': 29,
                      'Dentist': 30, 'Photographer': 31, 'Editor': 32, 'Stylist': 33,
                      'Software': 34, 'Accountant': 35}
education_mapping = {"Bachelor's": 0, "Master's": 1, "High School": 2, "Associate's": 3, "Doctoral": 4}
marital_status_mapping = {'Married': 0, 'Single': 1}
loan_status_mapping = {'Approved': 1, 'Denied': 0}

def load_data(file_name):
    # Especifica la ruta completa al archivo CSV
    file_path = '../data/loan.csv'
    
    # Cargar el archivo CSV
    data = pd.read_csv(file_path)
    
    return data

def preprocess_data(data):
    # Mapear las categorías a valores numéricos
    data['gender'] = data['gender'].map(gender_mapping)
    data['occupation'] = data['occupation'].map(occupation_mapping)
    data['education_level'] = data['education_level'].map(education_mapping)
    data['marital_status'] = data['marital_status'].map(marital_status_mapping)
    data['loan_status'] = data['loan_status'].map(loan_status_mapping)
    return data

def train_model(X_train, y_train):
    # Crear un imputador para rellenar los valores faltantes con la media
    imputer = SimpleImputer(strategy='mean')
    # Aplicar el imputador a los datos de entrenamiento
    X_train_imputed = imputer.fit_transform(X_train)
    # Create an instance of the Naive Bayes classifier
    nb = GaussianNB()
    # Entrenar el modelo Naive Bayes con los datos imputados
    nb.fit(X_train_imputed, y_train)
    return nb

def main():
    # Cargar los datos
    data = load_data('loan.csv')
    # Preprocesar los datos
    data = preprocess_data(data)
    # Separar las características y la variable objetivo
    X = data.drop(columns=['loan_status'])
    y = data['loan_status']
    # Dividir los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    # Entrenar el modelo
    model = train_model(X_train, y_train)
    # Evaluar el modelo
    accuracy = model.score(X_test, y_test)

    accuracy = accuracy * 100
    print("Accuracy:", accuracy , "%")
    
    # Guardar el modelo entrenado
    joblib.dump(model, 'modelo_entrenado2.pkl')

if __name__ == "__main__":
    main()
