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
 
with st.form( key="form_talent"):
        st.header("Input Data Talent")
        Nama = st.text_input("Nama Talent", placeholder="Input nama talent")
        effective_start_date = effective_start
        Grade = st.text_input("Grade", placeholder="Input grade")
    
            
        submit = st.form_submit_button("Input")
        if submit:
            long = len(Nama)
            Id_Talent = ("T"+Nama[0].upper()+Nama[long-1].upper()+str(creation_date_format))
            st.write(Id_Talent)
            st.write(long)
            if Nama and Grade and long >= 1:
                db.input_talent(Id_Talent,Nama,Grade,sysdate,effective_start_date,effective_end_dates)
                # st.write(db.input_talent(Id_Talent,Nama,Grade,sysdate,effective_start_date,effective_end_dates))
                st.success("Berhasil Di Input!")
                st.success("Nama : "+Nama)
                st.success("ID Talent: "+Id_Talent)
            else:
                st.warning("Field Harus Di Isi!")
        else:
            print("Belum Input")

                
with st.form(key="tampil talent"):
    search_nama = st.text_input("Cari Nama")         
    submit = st.form_submit_button("Cari Nama")
    st.subheader("Data Talent",divider="blue") 
    columns = ["ID Talent", "Nama", "Grade"]
    data = db.tampil_talent(search_nama,sysdate)
    df =  pd.DataFrame(data,columns=columns) 
    df["Pilih"] = False


edited_df = st.data_editor(
        df,
        column_config={
            "Pilih": st.column_config.CheckboxColumn("Pilih [Edit/Delete]")
        },
        use_container_width=True,
        hide_index=True
    )

selected = edited_df[edited_df["Pilih"] == True]
long_sel = len(selected)

with st.form(key="Edit"):
    st.subheader("Edit / Delete")
    col1, col2, col3 = st.columns(3)

    with col1:
        correct = st.form_submit_button("Correct")
    with col2:
        update = st.form_submit_button("Update")
    with col3:
        delete = st.form_submit_button("Delete")

    input1=""
    input2=""
    input3=""
    if not selected.empty:
        if  long_sel <= 1:
            input1 = st.text_input("Id Talent", value=selected.iloc[0]["ID Talent"])
            input2 = st.text_input("Nama", value=selected.iloc[0]["Nama"])
            input3 = st.text_input("Grade", value=selected.iloc[0]["Grade"])   
        else:
            st.warning("Pilih 1 Saja!")

    if update:
        if  input1 != "":
            db.update_talent(input1,effective_start_date)
            st.write("Update Berhasil ID "+ input1)
            db.input_talent(input1,input2,input3,sysdate,effective_start_date,effective_end_dates)      
        else:
            st.warning("Pilih 1!")  
    elif correct:
        if  input1 != "":
            db.correct_talent(input1,input3)
            st.write("Correct Berhasil ID "+ input1)
        else:
            st.warning("Pilih 1!")  
    elif delete:
         if  input1 != "":
            db.delete_talent(input1)
            st.write("Delete Berhasil ID "+ input1)
         else:
            st.warning("Pilih 1!")  
            
    
