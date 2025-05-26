import streamlit as st


import mysql.connector
import datetime
from mysql.connector import Error
import streamlit

hostname = "0-igg.h.filess.io"
database = "storage_costtownon"
port = "61002"
username = "storage_costtownon"
password = "c06342c974f010f014d095af8ebf435cbfd5beca"
sysdate =  datetime.datetime.now()
try:
    connection = mysql.connector.connect(host=hostname, database=database, user=username, password=password, port=port)
    if connection.is_connected():
        db_Info = connection.server_info
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
except Error as e:
    print("Error while connecting to MySQL", e)
# conn = st.connection("my_sql_connection", type="sql")

 

def input_talent(id, nama, grade, creation_date, effective_start_date, effective_end_date):
    
    try:
        cursor = connection.cursor()
        insert = cursor.execute("INSERT INTO list_talent (id_talent, nama, grade, creation_date, effective_start_date, effective_end_date) VALUES (%s, %s, %s, %s, %s, %s)",(id, nama, grade, creation_date, effective_start_date, effective_end_date))
        connection.commit()
        return insert
    except:
        print("Error")
    # return id, nama, grade, creation_date, effective_start_date, effective_end_date
    
def tampil_talent(nama,eff_date):
    
    try:
        cursor = connection.cursor()
        if nama:  # jika ada input pencarian
            cursor.execute("SELECT id_talent, nama, grade FROM list_talent WHERE nama LIKE %s and %s between effective_start_date and effective_end_date", ('%' + nama + '%',eff_date))
        else:  # jika tidak ada input, tampilkan semua
            cursor.execute("SELECT id_talent, nama, grade FROM list_talent where %s between effective_start_date and effective_end_date",(eff_date,))

        write = cursor.fetchall()
        return write

    except Exception as e:
        st.warning(f"Error: {e}")
        return []
        
# def correct_talent(id_talent,nama,grade):
    
#     try:
#         cursor = connection.cursor()
#         cursor.execute("update list_talent set nama=%s, grade=%s where id_talent = %s",(nama,grade,id_talent))
#         connection.commit()
#     except Exception as e:
#         st.warning(f"Error {e}")
        
def update_talent(id,effective_start_date):
    
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT MAX(creation_date) FROM list_talent WHERE id_talent=%s",(id,))
        max_creation_date = cursor.fetchone()[0]
        print(max_creation_date)
        cursor.execute("update list_talent  set effective_end_date=%s where id_talent = %s and creation_date = %s",(effective_start_date,id,max_creation_date))
        print("Updating")
                # insert = cursor.execute("INSERT INTO list_talent (id_talent, nama, grade, creation_date, effective_start_date, effective_end_date) VALUES (%s, %s, %s, %s, %s, %s)",(id, nama, grade, creation_date, effective_start_date, effective_end_date))
        connection.commit()
        print("update selesai")
    except Exception as e:
        st.warning(f"Error {e}")
        
        
def correct_talent(id,grade):
    try:
        cursor= connection.cursor
        cursor.execute("update list_talent  set grade=%s where id_talent = %s ",(id,grade))
        print("Correcting")
        connection.commit()
    except Exception as e:
        print(f"Error {e}")