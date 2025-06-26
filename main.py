 
import streamlit as st
import pandas as pd
import datetime
import db
 
  
def main():
  user = st.user
  if user:
    st.write("Email user login:"+ user )
  else:
    st.write("None")
  st.header("Marching Band Dunia Fantasi")
  st.image("stufan.jpg",caption="Stufan Dcorps")
 
if __name__ == '__main__':
 
        main()
    