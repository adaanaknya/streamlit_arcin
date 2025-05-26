import streamlit as st
import pandas as pd
import db
 

def main():
    st.title("Welcome!")

    st.write("Klik tombol di sidebar kiri untuk berpindah halaman.")

    # conn = st.connection("my_sql_connection", type="sql")
    # print(conn)
    # df = conn.query("SELECT * FROM storage",ttl=600)
    # st.write(pd.DataFrame(df)) 
    # st.write(df)
    
    if db.connection:
            st.write("Connected")
    else:
            st.write("Not Connected")
        

    
if __name__ == '__main__':
    main()
   
#     format streamlit connection
# type = "sql"
# # url = "mysql://username:password@host:port/database"