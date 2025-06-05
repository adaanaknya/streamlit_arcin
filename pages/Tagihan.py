import streamlit as st
import pandas as pd
import datetime
import db
 
st.set_page_config(layout="wide")
with st.form(key="Tagihan Per Period"):
    st.header("Tagihan Per Period") 
    
    nama = st.text_input("Nama")
    period = st.selectbox(
    "Periode Bulan",
    ("Januari", "Februari", "Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"),
    )
    columns = ["Nama", "Grade", "Period","Tahun","Tagihan"]
    tahun = st.text_input("Tahun")
    submit = st.form_submit_button("Cari")
    data = db.tagihan_period(nama,period,tahun)
    if submit:
        st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
    else:
         st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
         
         
with st.form(key="Tagihan Total"):
    st.header("Tagihan Total")   
    nama = st.text_input("Nama")
    submit = st.form_submit_button("Cari") 
    columns = ["Nama","Tagihan"]
    data = db.tagihan_total(nama)
    if submit:
        st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
    else:
         st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 