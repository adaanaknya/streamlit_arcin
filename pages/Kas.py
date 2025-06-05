import streamlit as st
import pandas as pd
import datetime
import db


creation_dates=  datetime.datetime.now()
creation_date_format = creation_dates.strftime('%Y%m%d%H%M%S')
sysdate = creation_dates.strftime('%Y-%m-%d %H:%M:%S')
effective_start= creation_dates.strftime('%Y-%m-%d')
effective_end_dates = "4712-12-31"
effective_end_date = datetime.datetime.strptime(effective_end_dates, "%Y-%m-%d").date()


st.set_page_config(layout="wide")
bulan_mapping = {
    "Januari": "01",
    "Februari": "02",
    "Maret": "03",
    "April": "04",
    "Mei": "05",
    "Juni": "06",
    "Juli": "07",
    "Agustus": "08",
    "September": "09",
    "Oktober": "10",
    "November": "11",
    "Desember": "12"
}
col1, col2 = st.columns(2)
cur = db.cur_amount()
st.write("Saldo Kas : " +str(cur))
with  col1:
    with st.form(key="Kas Masuk"):
        st.header("Kas Masuk")
        nama = st.text_input("Nama")
        keterangan = st.text_input("Keterangan")
        harga =  st.number_input("Harga / Nominal" ,step=1,format="%d")
        jumlah =  st.number_input("Jumlah" ,step=1,format="%d")
        tanggal = st.date_input("Tanggal")
        submit = st.form_submit_button("Input") 
        if submit:
            if nama and keterangan and harga and jumlah and tanggal:
                db.input_kas_masuk(creation_date_format,nama,keterangan,harga,jumlah,tanggal)
            else:
                st.warning("Isi semua field!")
        
with col2:
    with st.form(key="Kas Keluar"):
        st.header("Kas Keluar")
        nama = st.text_input("Nama")
        keterangan = st.text_input("Keterangan")
        harga =  st.number_input("Harga / Nominal" ,step=1,format="%d")
        jumlah =  st.number_input("Jumlah" ,step=1,format="%d")
        tanggal = st.date_input("Tanggal")
        submit = st.form_submit_button("Input") 
        if submit:
            if nama and keterangan and harga and jumlah and tanggal:
                db.input_kas_keluar(creation_date_format,nama,keterangan,harga,jumlah,tanggal)
            else:
                st.warning("Isi semua field!")
                
                
with st.form(key="History"):
    period = st.selectbox(
    "Periode Bulan",
    ("Januari", "Februari", "Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"),
    )
 
    tahun = st.text_input("Tahun")
    
    columns = ["Nama", "Keterangan", "Harga / Nominal","Jumlah","Tanggal","Komponen","Total"]
    submit = st.form_submit_button("Cari") 
    if submit:
        if period in bulan_mapping:
            periods = bulan_mapping[period]
            data = db.history_kas(periods,tahun)
            if period and tahun:
                st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
            else:
                st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True)   
    
       