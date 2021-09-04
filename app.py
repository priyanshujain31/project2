import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
pickle_in = open("project2.pkl","rb")
model=pickle.load(pickle_in)
dataset= pd.read_csv('winequality-red.csv')



X = dataset.iloc[:,0:11].values

def predict_note_authentication(fixedacidity,volatileacidity,citricacid,	residualsugar,	chlorides,	freesulfurdioxide,	totalsulfurdioxide,	density,pH,sulphates,alcohol):
  output= model.predict([[fixedacidity,volatileacidity,citricacid,	residualsugar,	chlorides,	freesulfurdioxide,	totalsulfurdioxide,	density,pH,sulphates,alcohol]])
  print("Wine Quality =", output)
  if output==[1]:
    prediction="Good Quality Wine"
  else:
    prediction="Bad Quality Wine"
  print(prediction)
  return prediction
def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;">Machine Learning Project</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Wine Quality Prediction")

    fixedacidity=st.number_input('Insert fixedacidity',0.0)
   
    volatileacidity=st.number_input('Insert volatileacidity',0.0)
    
    citricacid=st.number_input('Insert citricacid',0.0)
    residualsugar=st.number_input('Insert residualsugar',0.0)
    chlorides=st.number_input('Insert chlorides',0.0)
    freesulfurdioxide=st.number_input('Insert freesulfurdioxide',0.0)
    totalsulfurdioxide=st.number_input('Insert totalsulfurdioxide',0.0)
    density=st.number_input('Insert density',0.0)
    pH=st.number_input('Insert pH',0.0)
    sulphates=st.number_input('Insert sulphates',0.0)
    alcohol=st.number_input('Insert alcohol',0.0)

    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(fixedacidity,volatileacidity,citricacid,	residualsugar,	chlorides,	freesulfurdioxide,	totalsulfurdioxide,	density,pH,sulphates,alcohol)
      st.success('Model has predicted = {}'.format(result))
    if st.button("About"):
      st.subheader("Developed by Priyanshu Jain")
      st.subheader("C-Section,PIET")

if __name__=='__main__':
  main()
   
