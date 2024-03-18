import streamlit as st
import pandas as pd
import numpy as np
from src.pipeline.predict_pipeline import CustomData,  PredictPipeline

st.title(':blue[Student Exam Performance Prediction] :male-student:')
st.divider()

choice_gender = {"male":"Male", "female":"Female"}
# def format_func(dictory:dict ,option):
#     return dictory[option]

gender = st.selectbox(
    'Gender ?',
    options=list(choice_gender.keys()),
    format_func= lambda x : choice_gender[x],
    index=None,
)
st.write('You selected:', gender)

choice_race = {"group A": "Group A", "group B":"Group B", "group C":"Group C", "group D":"Group D", "group E":"Group E"}
race_or_ethnicity = st.selectbox(
    'Race or Ethnicity ?',
    options=list(choice_race.keys()),
    format_func= lambda x : choice_race[x],
    index=None,
)
st.write('You selected:', race_or_ethnicity)

parental_level_of_education = st.selectbox(
    'Parental Level of Education ?',
    ('associate\'s degree', 'bachelor\'s degree', 'high school', 'master\'s degree', 'some college', 'some high school'),
    index=None,
)
st.write('You selected:', parental_level_of_education)

lunch = st.selectbox(
    'Lunch Type ?',
    ('free/Reduced', 'standard'),
    index=None,
)
st.write('You selected:', lunch)

test_preparation_course = st.selectbox(
    'Test preparation course',
    ('none', 'completed'),
    index=None
)
st.write('You selected:', test_preparation_course)

reading_score = st.number_input(
    'Reading score out of 100',
    min_value=0,
    max_value=100
)
st.write('You selected:', reading_score)

writing_score = st.number_input(
    'Writing score out of 100',
    min_value=0,
    max_value=100,
)
st.write('You selected:', writing_score)

if st.button('Predict'):
    data = CustomData(
        gender=gender,
        race_ethnicity=race_or_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_dataframe()
    st.write(pred_df)
    predict_pipeline = PredictPipeline()
    results = predict_pipeline.predict(pred_df)
    st.write('Students math score will be ', results[0])
else:
    st.write('Inset value and submit')







