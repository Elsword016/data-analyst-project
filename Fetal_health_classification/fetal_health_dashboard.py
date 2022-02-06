from anyio import open_cancel_scope
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
#from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

pickle_in = open('model_pkl','rb')
clf = pickle.load(pickle_in)

##Creating the Streamlit UI
st.sidebar.header('Fetal health Classification')
select = st.sidebar.selectbox('Select instance',['Form 1'],key='1')
if not st.sidebar.checkbox("Hide", True,key='1'):
    st.title('Fetal Health')
    name = st.text_input("Name of doctor:")
    baselineval = st.number_input("Baseline Value")
    accelarations = st.number_input("Accelerations")
    fetal_movement = st.number_input("Fetal Movement")
    ut_contract = st.number_input("Uterine Contractions")
    lgt_decc = st.number_input("Light decceleration")
    sev_dcc = st.number_input("Severe deccelerations")
    prol_dcc = st.number_input("Prolonged deccelarations")
    ab_stv = st.number_input("abnormal_short_term_variability")
    mval_ab = st.number_input("mean_value_of_short_term_variability")
    perc = st.number_input("percentage_of_time_with_abnormal_long_term_variability")
    mval_ab2 = st.number_input("mean_value_of_long_term_variability")
    hwidth = st.number_input("histogram_width")
    hmin = st.number_input("histogram_min")
    hmax = st.number_input("histogram max")
    hpeaks = st.number_input("histogram_no_of_peaks")
    hzeros =  st.number_input("histogram_number_of_zeroes")
    hmode = st.number_input("histogram_mode")
    hmean = st.number_input("histogram_mean")
    hmedian = st.number_input("histogram median")
    hvar = st.number_input("histogram_variance")
    htend = st.number_input("histogram_tendency")

submit = st.button("Predict")

if submit:
    prediction = clf.predict([[baselineval,accelarations,fetal_movement,ut_contract,lgt_decc,sev_dcc,prol_dcc,ab_stv,mval_ab,perc,mval_ab2,hwidth,hmin,hmax,hpeaks,hzeros,hmode,hmean,hmedian,hvar,htend]])

    if prediction == 1:
        st.write("Fetal Health conditon >>>> Normal")
    elif prediction == 2:
        st.write("Fetal health condition >>>> Suspected to have a pathology")
    else:
        st.write("Fetal health condition >>>> Medical Attention immediate!")



