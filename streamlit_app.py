import streamlit as st
import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Definir características categóricas y numéricas
categorical_features = ['M/F']
numeric_features = ['MR Delay', 'Age', 'EDUC', 'SES', 'MMSE', 'CDR', 'eTIV', 'nWBV', 'ASF']

# Preprocesador para transformar las columnas categóricas y numéricas
preprocessor = ColumnTransformer(
    transformers=[
        ('num', Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ]), numeric_features),
        ('cat', OneHotEncoder(drop='first'), categorical_features)
    ]
)

# Cargar los modelos
lr_150 = joblib.load('modelo/best_lr_model_150.pkl')
lr_373 = joblib.load('modelo/best_lr_model_373.pkl')
svm_150 = joblib.load('modelo/best_svm_model_150.pkl')
svm_373 = joblib.load('modelo/best_svm_model_373.pkl')

# Interfaz del usuario
st.title("OASIS DATASET - ALZHEIMER PREDICTION")

# Entradas del usuario
mr_delay = st.number_input("MR Delay")
age = st.number_input("Age")
educ = st.number_input("Years of Education")
ses = st.number_input("Socioeconomic Status")
mmse = st.number_input("Mini-Mental State Examination Score")
cdr = st.number_input("Clinical Dementia Rating")
etiv = st.number_input("Estimated Total Intracranial Volume")
nwbv = st.number_input("Normalized Whole-Brain Volume")
sex = st.selectbox("Gender", ['M', 'F'])
asf = st.number_input("Atlas Scaling Factor")

# DataFrame con las entradas del usuario
input_df = pd.DataFrame({
    'MR Delay': [mr_delay],
    'Age': [age],
    'EDUC': [educ],
    'SES': [ses],
    'MMSE': [mmse],
    'CDR': [cdr],
    'eTIV': [etiv],
    'nWBV': [nwbv],
    'ASF': [asf],
    'M/F': [sex]  # Cambié 'sex' a 'M/F' para que coincida con el preprocesador
})

# Seleccionar modelo
models = {
    "Linear Regression with 150 dataset": lr_150,
    "Linear Regression with 373 dataset": lr_373,
    "Support Vector Machine with 150 dataset": svm_150,
    "Support Vector Machine with 373 dataset": svm_373
}

selected_model = st.selectbox("Select the model you prefer", list(models.keys()))

# Predicción
if st.button("Predict"):
    try:
        # Aplicar el preprocesador a los datos de entrada
        input_processed = preprocessor.fit_transform(input_df)  # Cambiado a fit_transform

        # Seleccionar el modelo
        model = models[selected_model]

        # Realizar la predicción
        prediction = model.predict(input_processed)

        # Mostrar la predicción
        st.write(f"The prediction of {selected_model} is: {prediction[0]}")
    except Exception as e:
        st.error(f"Prediction error: {e}")