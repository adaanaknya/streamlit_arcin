 
import streamlit as st
import pandas as pd
import datetime
import db
import gspread
from oauth2client.service_account import ServiceAccountCredentials

 
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("kas-stufan-637642aa5c98.json", scope)
client = gspread.authorize(creds)
sheet = client.open("API")
worksheet = sheet.sheet1
data = worksheet = sheet.sheet1.get_all_records()
def main():
  
  st.header("Marching Band Dunia Fantasi")
  st.image("stufan.jpg",caption="Stufan Dcorps")
  st.write("📊 Data dari Google Sheets:", data)
        
if __name__ == '__main__':
 
        main()
    