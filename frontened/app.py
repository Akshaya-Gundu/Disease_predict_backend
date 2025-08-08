import streamlit as st
import requests
#st.title("Heart disease prediction")
disease=st.selectbox("Select disease",["Heart","diabetes"])
if disease=="Heart":
    st.title("Heart disease prediction")
    age=st.slider("Age",20,90)
    sex=st.selectbox("sex",[0,1])
    cp=st.selectbox("Chest Pain type",[0,1,2,3])
    trestbps=st.slider("Resting BP",90,200)
    chol=st.slider("cholesterol",100,400)
    fbs=st.selectbox("Fasting blood sugar>120",[0,1])
    restecg=st.selectbox("Rest ECG",[0,1,2])
    thalach=st.slider("Max heart rate",72,200)
    exang=st.selectbox("Exercise Induces Angina",[0,1])
    oldpeak=st.slider("oldpeak",0.6,6.0)
    slope=st.selectbox("Sahpe",[0,1,2])
    ca=st.selectbox("CA",[0,1,2,3,4])
    thal=st.selectbox("Thal",[0,1,2])
    features=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    endpoint="http://localhost:8000/heart_pred"
elif disease=="diabetes": 
    st.title("diabetes Prediction")
    Pregnancies=st.slider("Pregnancies",0,10)
    glu=st.selectbox("Glucose",[0,1,2,3])
    bp=st.slider("BP",70,300)
    skin=st.slider("skin thickness",0,45)
    insu=st.slider("Insulin",0.04,1.50)
    bmi=st.selectbox("BMI",[0,1,2])
    dia=st.slider("diabets",0.061,3.00)
    age=st.slider("Age",35,65)
    features=[Pregnancies,glu,bp,skin,insu,age,bmi,dia]
    endpoint="http://localhost:8000/diabetes_pred"
if st.button("predict"):
    response=requests.post(endpoint,json=features)
    if response.status_code==200:
        risk=response.json()['risk_score']
        st.success(f"Risk score:{risk:.2f}")
    else:
        st.error(f"Error:{response.text}")
