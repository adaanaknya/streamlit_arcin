 
import streamlit as st
import pandas as pd
import datetime
import db
 
user = st.experimental_user
def main():


  if user is None:
      st.warning("User belum terdeteksi. Coba login dulu ke https://streamlit.io/cloud lalu akses ulang app.")
  else:
        st.write("📧 Email:", getattr(user, "email", "Tidak ada"))
        st.write("🆔 User ID:", getattr(user, "user_id", "Tidak ada"))
  st.header("Marching Band Dunia Fantasi")
  st.image("stufan.jpg",caption="Stufan Dcorps")
 
if __name__ == '__main__':
 
        main()
    