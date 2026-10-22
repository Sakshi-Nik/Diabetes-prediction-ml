import os
import warnings
import joblib
import pandas as pd
import streamlit as st
from sklearn.exceptions import InconsistentVersionWarning

warnings.filterwarnings("ignore", category=InconsistentVersionWarning)

st.set_page_config(page_title="Diabetes Prediction", page_icon="🩺", layout="centered")

MODEL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "random_forest_model.pkl")
FEATURES = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"
]

@st.cache_resource
def load_model():
    # This model was saved with scikit-learn 1.7.2; requirements.txt pins that version.
    return joblib.load(MODEL_PATH)

st.title("🩺 Diabetes Prediction")
st.write("Enter the patient features and click **Predict**.")


if not os.path.exists(MODEL_PATH):
    st.error("Model file is missing. Keep random_forest_model.pkl beside app.py.")
    st.stop()

try:
    model = load_model()
except Exception as exc:
    st.error(f"Could not load the model: {exc}")
    st.info("Install the packages from requirements.txt in this project's virtual environment, then restart the app.")
    st.stop()

with st.form("prediction_form"):
    st.subheader("Patient Features")
    left, right = st.columns(2)
    with left:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
        glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, max_value=300.0,  step=1.0)
        bp = st.number_input("Blood Pressure (mm Hg)", min_value=0.0, max_value=200.0, step=1.0)
        skin = st.number_input("Skin Thickness (mm)", min_value=0.0, max_value=100.0,  step=1.0)
    with right:
        insulin = st.number_input("Insulin (mu U/ml)", min_value=0.0, max_value=900.0,  step=1.0)
        bmi = st.number_input("BMI", min_value=0.0, max_value=80.0,  step=0.1)
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0,  step=0.01)
        age = st.number_input("Age (years)", min_value=1, max_value=120, step=1)
    submitted = st.form_submit_button("Predict", type="primary", use_container_width=True)

if submitted:
    data = pd.DataFrame(
        [[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]],
        columns=FEATURES
    )
    try:
        prediction = int(model.predict(data)[0])
        st.subheader("Result")
        if prediction == 1:
            st.error("Prediction: Diabetic")
        else:
            st.success("Prediction: Non-diabetic")
        if hasattr(model, "predict_proba"):
            probabilities = model.predict_proba(data)[0]
            classes = list(model.classes_)
            if 1 in classes:
                positive_score = float(probabilities[classes.index(1)])
                st.write(f"Model's estimated positive-class score: **{positive_score:.1%}**")
       
    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
        st.info("Confirm that the model file matches scikit-learn 1.7.2 and uses these eight features.")
