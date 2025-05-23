import streamlit as st
import pickle
import numpy as np

st.title('Heart Disease Predictor')
st.image('image.png', caption= 'Predict Your Heart Disease')

with open ('heartdiseasepickle.pkl', 'rb') as pickleFile:
    model = pickle.load(pickleFile)

# def predictionFunction(age,	cp,	restecg,	thalach,	exang):
#     try:
#         prediction = model.predict([[age,	cp,	restecg,	thalach,	exang]])
#         return 'Disease not found' if prediction[0]==1 else 'Disease found'
#     except Exception as e:
#         return f'Error:{str(e)}'

st.sidebar.header('How to Use!')
st.sidebar.markdown("""
1. Enter the heart details.
2. Click 'Predict' to See the Result.
3. Adjust Values to Test Different Scenarios.
""")

# def main():
st.subheader('Enter your detail')
age = st.number_input("Age", min_value=20, max_value=100, value=50)
sex = st.radio('sex:', options=['Male', 'Female'] )
cp = st.selectbox("Chest Pain Type (cp)", [0, 1, 2, 3], help="0: typical angina, 1: atypical, 2: non-anginal, 3: asymptomatic")
restecg = st.selectbox("Resting ECG Result (restecg)", [0, 1, 2], help="0: normal, 1: ST-T wave abnormality, 2: left ventricular hypertrophy")
thalach = st.slider("Max Heart Rate Achieved (thalach)", min_value=70, max_value=210, value=150)
exang = st.selectbox("Exercise Induced Angina (exang)", [0, 1], help="0: No, 1: Yes")
if st.button("Predict"):
    # 5. Prepare input for model (as array)
    input_data = np.array([[age, cp, restecg, thalach, exang]])
    
    # 6. Make prediction
    prediction = model.predict(input_data)[0]
    
    # 7. Show result
    if prediction == 1:
        st.error("Warning: You may have a heart disease.")
    else:
        st.success("Great! You likely do not have heart disease.")
    # if st.button('Predict'):
    #     result = predictionFunction(age,	cp,	restecg,	thalach,	exang)
    #     st.markdown(f'{result}')
    #     st.balloons()

# if __name__ == '__main__':
#     main()
