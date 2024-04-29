import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = pickle.load(open('finalized_model.pkl', 'rb'))

# Main function for Streamlit app
def main():
    st.title("Hypertension Prediction")

    # User inputs with descriptive text
    age = st.number_input("Age", min_value=0, max_value=120, step=1)
    sex = st.selectbox("Sex", ['Male', 'Female'])
    cholesterol = st.number_input("Cholesterol", min_value=100, max_value=400, step=1)
    diabetes = st.selectbox("Diabetes", ['No', 'Yes'])
    smoking = st.selectbox("Smoking", ['No', 'Yes'])
    obesity = st.selectbox("Obesity", ['No', 'Yes'])
    alcohol_consumption = st.selectbox("Alcohol Consumption", ['No', 'Yes'])
    exercise_hours = st.number_input("Exercise Hours Per Week", min_value=0.0, max_value=40.0, step=0.1)
    diet = st.selectbox("Diet", ['Healthy', 'Average', 'Unhealthy'])
    income = st.number_input("Income", min_value=0, max_value=1000000, step=1000)
    bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
    physical_activity_days = st.number_input("Physical Activity Days Per Week", min_value=0, max_value=7, step=1)
    sleep_hours = st.number_input("Sleep Hours Per Day", min_value=0, max_value=24, step=1)
    country = st.selectbox("Country", ['South Africa', 'Nigeria'])

    # Prepare input data for prediction
    input_features = {
        'Age': age,
        'Sex': 1 if sex == 'Male' else 0,
        'Cholesterol': cholesterol,
        'Diabetes': 1 if diabetes == 'Yes' else 0,
        'Smoking': 1 if smoking == 'Yes' else 0,
        'Obesity': 1 if obesity == 'Yes' else 0,
        'Alcohol Consumption': 1 if alcohol_consumption == 'Yes' else 0,
        'Exercise Hours Per Week': exercise_hours,
        'Diet': {'Healthy': 0, 'Average': 1, 'Unhealthy': 2}[diet],
        'Income': income,
        'BMI': bmi,
        'Physical Activity Days Per Week': physical_activity_days,
        'Sleep Hours Per Day': sleep_hours,
        'Country': 0 if country == 'South Africa' else 1
    }

    # Prediction button
    if st.button('Predict Hypertension'):
        input_df = pd.DataFrame([input_features])
        prediction = model.predict(input_df)

        if prediction[0] == 1:
            st.success('The patient is likely to have hypertension.')
        else:
            st.success('The patient is likely not to have hypertension.')

if __name__ == '__main__':
    main()
