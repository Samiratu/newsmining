 
import pickle
import streamlit as st
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import LabelEncoder
label_enc = LabelEncoder()


# clean_doc=pickle.load(open('clean_doc.obj','rb'))
tfid= pickle.load(open('Tfidfmodels2.pkl','rb'))
model=pickle.load(open('kmeanmodel.pkl','rb'))
# data= pd.read_csv('https://raw.githubusercontent.com/Diane10/news_classifier/main/All_combined_New_papers%20-%20Sheet1.csv')
      
# front end elements of the web page 
html_temp = """ 
<div style ="background-color:yellow;padding:13px"> 
<h1 style ="color:black;text-align:center;">Streamlit Loan Prediction ML App</h1> 
</div> 
""" 
st.markdown(html_temp, unsafe_allow_html = True) 
default_value_goes_here = ""
Content = st.text_area("label goes here", default_value_goes_here)
result =""
df= pd.read_csv('https://raw.githubusercontent.com/Samiratu/DataMining_Visualizations/main/finaldata.csv')
# data["label"] = label_enc.fit_transform(data[["label"]])  
# when 'Predict' is clicked, make the prediction and store it 
if st.button("Predict"): 
  pred = model.predict(tfid.transform([Content]))
  if pred==1:
    st.write('sports')   
    pred= int(pred)
    data_pred = df.loc[(df['pred_label'] == pred)]
    # df[df['pred_label']==pred ]['link'].unique()
    st.markdown(data_pred['link'].unique())
  elif pred==0:
    st.write('entertainment')
    term="entertainment"
    pred= int(pred)
    data_pred = df.loc[(df['pred_label'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.markdown(data_pred['link'].unique())
  elif pred==2:
    st.write('politics') 
    pred= int(pred)
    term="politics"
    pred= int(pred)

    data_pred = df.loc[(df['pred_label'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.markdown(data_pred['link'].unique())
  elif pred==3:
    st.write('culture')
    pred= int(pred)
    term='culture'
    pred= int(pred)

    data_pred = df.loc[(df['pred_label'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.markdown(data_pred['link'].unique())
  elif pred==4:
    st.write('business')
    pred= int(pred)
    term='business'
    data_pred = df.loc[(df['pred_label'] == pred)]
    # result_df= data_pred[data_pred['source_url'].str.contains(term)]
    st.markdown(data_pred['link'].unique())