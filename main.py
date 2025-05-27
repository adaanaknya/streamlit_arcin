"""
# Report Summary
"""
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


def main():
  st.header("Marching Band Dunia Fantasi")
  st.page_link("pages/Data_Talent.py", label="Home", icon="🏠")
  

        
if __name__ == '__main__':
    # if st.session_state.get('authentication_status'):
        main()
    # else:
    #     st.warning("Silahkan Login Terlebih Dahulu!")
