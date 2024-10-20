import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

Taitanic = pickle.load(open('model.pkl', 'rb'))

st.title('Logistic Regression Assignment')

# Pclass Sex Age SibSp Parch Fare Embarked
Pclass = st.number_input('Pclass')
Sex = st.text_input('Sex')
Age = st.number_input('Age')
SibSp = st.number_input('SibSp')
Parch = st.number_input('Parch')
Fare = st.number_input('Fare')
Embarked = st.text_input('Embarked') 

if st.button('predict'):
    data = {'Pclass': Pclass, 'Sex': Sex, 'Age': Age, 'SibSp': SibSp, 'Parch': Parch, 'Fare': Fare, 'Embarked': Embarked}
    df = pd.DataFrame([data])
    
    
    # predict
    prediction = Taitanic.predict(df)
    
    
    if prediction[0] == 0:
      st.error('The passenger is predicted to not survive the Titanic disaster.')
    else:
      st.success('The passenger is predicted to survive the Titanic disaster.')