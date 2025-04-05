# 🩺 Health Risk Prediction Using Machine Learning
A machine learning-based web application to predict the likelihood of health risks based on user input such as age, BMI, blood pressure, lifestyle choices, and more. The application uses multiple classification models and provides predictions through a simple Streamlit web interface.

 
# 🚀 Features
Predict health risk (1 = risk, 0 = no risk) based on user input

Implements multiple ML models:

Logistic Regression

Decision Tree Classifier

Random Forest Classifier

Visual comparison of model performance

Clean and interactive UI using Streamlit

End-to-end project: data preprocessing, model training, evaluation, and deployment
 
 # 📁 Repository Structure

 Health_risk-main/
│
├── Health Risk Prediction.ipynb    # Jupyter notebook with EDA and model training
├── health.csv                      # Dataset used for training and testing
├── model.pkl                       # Saved ML model (Random Forest)
├── app.py                          # Streamlit application file
├── requirements.txt                # Required Python libraries
└── README.md                       # Project documentation

# 📊 Dataset Description

The dataset (health.csv) contains the following features:

Age

Gender

Sleep Duration

Quality of Sleep

Physical Activity Level

Stress Level

BMI Category

Heart Rate

Daily Steps

Smoking Habit

Alcohol Consumption

Occupation

Health Risk (Target variable)

#  🧠 Models Used

Logistic Regression

Decision Tree Classifier

Random Forest Classifier (final deployed model)

Each model was evaluated using:

Accuracy

Precision

Recall

F1-score

The Random Forest model performed the best and was saved as model.pkl for deployment.

# 🖥️ How to Run the Project

# Clone the Repository

git clone : https://github.com/HarshRay04/Health_risk-main.git
cd Health_risk-main

# Install Dependencies

It is recommended to use a virtual environment.

pip install -r requirements.txt

# Run the Streamlit App

streamlit run app.py

# Interact with the App

Enter your health details through the sliders and dropdowns.

Get an instant prediction on your health risk status.

# 📷 Screenshots



# 🔮 Future Enhancements

Add more health-related features to improve prediction accuracy

Support multi-class health condition predictions

Enable model selection through UI

Deploy the app on cloud platforms like Heroku or Streamlit Cloud

# 📌 Requirements
Python 3.7+

Pandas

NumPy

Scikit-learn

Matplotlib

Streamlit

Joblib

All dependencies are listed in requirements.txt.

# 🤝 Acknowledgements

Streamlit

Scikit-learn

The dataset source (add link if publicly available)

# 📬 Contact
Author: Harsh Ray
Email: harshray04@gmail.com || 22052297@kiit.ac.in
GitHub: [@HarshRay04](https://github.com/HarshRay04)

