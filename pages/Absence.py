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
    "Januari": 1,
    "Februari": 2,
    "Maret": 3,
    "April": 4,
    "Mei": 5,
    "Juni": 6,
    "Juli": 7,
    "Agustus": 8,
    "September": 9,
    "Oktober": 10,
    "November": 11,
    "Desember": 12
}


st.header("Rekap Parade")
with st.form(key="input absence"):
    users_dict = db.lov_nama(sysdate)
    nama_talent = st.selectbox("Pilih Nama:", list(users_dict.keys()))
    id_talent = users_dict[nama_talent]  
    
    # grade = st.text_input("grade",value=grades)
    period = st.selectbox(
    "Periode Bulan",
    ("Januari", "Februari", "Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"),
    )
    tahun = st.text_input("Tahun")
    jumlah_main =  st.number_input("Jumlah Main" ,step=1,format="%d")
    submit = st.form_submit_button("Submit")
  
        
    if submit:
        if period in bulan_mapping and tahun:
            id_abs = ("ABS"+str(creation_date_format))
            tahuns = int(tahun)
            bulan_start = bulan_mapping[period]
            bulan_end = bulan_mapping[period]+ 1
            start_date = datetime.datetime(tahuns, bulan_start, 26)
            end_date = datetime.datetime(tahuns, bulan_end, 25)
            if tahun and period and jumlah_main:
                grades = db.load_grade(start_date,id_talent)
                tagihan =0
                if grades =="C":
                    tagihan = jumlah_main * 10000
                elif grades =="B":
                    tagihan = jumlah_main * 5000
                elif grades =="A":
                    tagihan = jumlah_main * 0
                db.input_absence(id_talent,grades,jumlah_main,sysdate,period,tagihan,start_date,end_date,id_abs)
                st.success("Berhasil di Input!")
            else:
                st.warning("Isi semua field")
        else:
            st.warning("isis semua field")
 
 
with st.form(key="History"):
    abs = ""
    
    period = st.selectbox(
    "Periode Bulan",
    ("Januari", "Februari", "Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"),
    )

    tahun = st.text_input("Tahun")
    columns = ["ID","Nama", "Grade", "Periode","Tahun","Jumlah Main"]
    submit = st.form_submit_button("Cari") 
    # if submit:
    
    if submit:
        data = db.history_absence(period,tahun)
        df =  pd.DataFrame(data,columns=columns) 
        df["Pilih"] = False  
    else:
        data = db.history_absence(period,tahun)
        df =  pd.DataFrame(data,columns=columns) 
        df["Pilih"] = False
            
edited_df = st.data_editor(
        df,
        column_config={
            "Pilih": st.column_config.CheckboxColumn("Pilih [Delete]")
        },
        use_container_width=True,
        hide_index=True)
selected = edited_df[edited_df["Pilih"] == True]

long_sel = len(selected)    
id_absence = selected["ID"].tolist()
abs =id_absence
            
    
# st.write(abs)
delete = st.button("Hapus")
if delete:
    db.delete_absence(id_absence)
    st.rerun()         

    