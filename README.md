# 🩺 Diabetes Prediction Using Machine Learning

A machine learning-based web application that predicts the possibility of diabetes using patient health parameters. The project uses a **Random Forest Classifier** trained on the Pima Indians Diabetes Dataset and provides an interactive interface built with **Streamlit**.

## 🚀 Live Demo

🔗 **[Try the Diabetes Prediction App](https://diabetes-prediction-ml-cm57xq8jfv9rqnsnwqng77.streamlit.app/)**

## 📌 Project Overview

Diabetes is a chronic health condition that requires early detection and proper management. This project demonstrates how machine learning can be used to classify diabetes outcomes based on medical and health-related input features.

Users can enter patient information into the web application and receive a prediction from the trained Random Forest model.

## 🎯 Objectives

- Develop a machine learning model for diabetes prediction.
- Perform data preprocessing and model training.
- Use a Random Forest Classifier for prediction.
- Build an interactive web interface using Streamlit.
- Deploy the application online for easy access.

## 📊 Dataset

**Dataset:** Pima Indians Diabetes Database

**Source:** Kaggle

🔗 [Download Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)

The dataset contains 768 patient records with the following eight input features and one target variable.

| Feature | Description |
|---|---|
| Pregnancies | Number of pregnancies |
| Glucose | Plasma glucose concentration |
| BloodPressure | Diastolic blood pressure |
| SkinThickness | Triceps skin fold thickness |
| Insulin | 2-hour serum insulin |
| BMI | Body Mass Index |
| DiabetesPedigreeFunction | Diabetes pedigree function |
| Age | Patient's age |

**Target Variable:** `Outcome`
- `0` – Non-diabetic
- `1` – Diabetic

## 🛠️ Technology Stack

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Algorithm:** Random Forest Classifier
- **Data Processing:** Pandas, NumPy
- **Web Framework:** Streamlit
- **Model Serialization:** Joblib
- **Deployment:** Streamlit Community Cloud
- **Version Control:** Git and GitHub

## ⚙️ Machine Learning Workflow

1. Dataset collection
2. Data preprocessing
3. Feature selection
4. Model training using Random Forest Classifier
5. Model evaluation
6. Saving the trained model as a `.pkl` file
7. Integrating the model with Streamlit
8. Deploying the application

## 📸 Application Screenshots

### Diabetes Prediction Interface

![Diabetes Prediction App Screenshot](screenshots/diabetes-prediction.png)

### Prediction Result

_Add a screenshot showing the prediction result here._

## 💻 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/Sakshi-Nik/Diabetes-prediction-ml.git
```

### 2. Navigate to the project directory

```bash
cd Diabetes-prediction-ml
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux/macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

## 📁 Project Structure

```text
Diabetes-prediction-ml/
│
├── app.py
├── random_forest_model.pkl
├── requirements.txt
├── screenshots/
│   └── diabetes-prediction.png
└── README.md
```

## 🔮 Future Enhancements

- Add model performance visualizations.
- Compare multiple machine learning algorithms.
- Add prediction history and downloadable reports.
- Improve the user interface with an interactive dashboard.
- Add additional model evaluation metrics.

## ⚠️ Disclaimer

This project is developed for educational and academic purposes. The predictions are not medical diagnoses and should not replace professional medical advice.

## 👩‍💻 Author

**Swati Patil**

GitHub: [Sakshi-Nik](https://github.com/Sakshi-Nik)

Project Repository: [Diabetes Prediction ML](https://github.com/Sakshi-Nik/Diabetes-prediction-ml)

---

⭐ If you find this project useful, consider giving the repository a star!
