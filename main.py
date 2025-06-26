 
import streamlit as st
import pandas as pd
import datetime
import db
 
user = st.user
def main():


  if user is None:
      st.warning("User belum terdeteksi. Coba login dulu ke https://streamlit.io/cloud lalu akses ulang app.")
  else:
      st.success(f"Login sebagai: {user} ")
      st.write(user)
  st.header("Marching Band Dunia Fantasi")
  st.image("stufan.jpg",caption="Stufan Dcorps")
 
if __name__ == '__main__':
 
        main()
    