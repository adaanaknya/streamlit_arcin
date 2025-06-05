 
import streamlit as st
import pandas as pd
import datetime
import db
from st_aggrid import AgGrid,GridOptionsBuilder

 

  

def main():
  st.set_page_config(page_title="Home")
  st.header("Marching Band Dunia Fantasi")
  st.image("stufan.jpg",caption="Stufan Dcorps")
  df = pd.DataFrame({
    'Nama': ['Andi', 'Budi', 'Citra'],
    'Umur': [25, 30, 28]
})

  st.write("### Daftar Pengguna")

  # Tampilkan tabel + tombol per baris
  for i, row in df.iterrows():
      col1, col2, col3 = st.columns([3, 1, 1])
      with col1:
          st.write(f"{row['Nama']} (Umur: {row['Umur']})")
      with col2:
          if st.button("Edit", key=f"edit_{i}"):
              st.success(f"Edit {row['Nama']}")
      with col3:
          if st.button("Hapus", key=f"delete_{i}"):
              st.warning(f"Hapus {row['Nama']}")


        
if __name__ == '__main__':
 
        main()
    