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
with st.form(key="Pembayaran"):
    st.header("Form Pembayaran")
    users_dict = db.lov_nama(sysdate)
    nama_talent = st.selectbox("Pilih Nama:", list(users_dict.keys()))
    id_talent = users_dict[nama_talent] 
    keterangan = st.selectbox(
    "Cash / Transfer",
    ("Cash", "Transfer"))
    tanggal = st.date_input("Tanggal")
    nominal =  st.number_input("Jumlah Bayar (Dalam rupiah tanpa titik contoh 5000)" ,step=1,format="%d")
    submit = st.form_submit_button("Input")
    if submit:
        if nama_talent and keterangan and nominal and tanggal:
            db.input_pembayaran(creation_date_format,id_talent,keterangan,sysdate,nominal,tanggal)
            st.success("Data Behasil di input")
            
        else:
            st.warning("Field Harus Di isi semua")
            
with st.form(key="history pembayaran"):
    st.header("History Pembayaran")   
    nama = st.text_input("Nama")
    date_from = st.date_input("Date From")
    date_to = st.date_input("Date To")
    submit = st.form_submit_button("Cari") 
    columns = ["Nama","Keterangan","Nominal","Tanggal"]
    data = db.history_pembayaran(nama,date_from,date_to)
    if submit:
        st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
    else:
         st.dataframe(pd.DataFrame(data,columns=columns),hide_index=True) 
         
    calculate = st.form_submit_button("Calculate")
    result = db.calculate(date_from,date_to)
    if calculate:
        st.write("Total = "+result)