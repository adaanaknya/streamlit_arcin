import main
import connection
import streamlit as st


def start():
    pilih = int(input("Input : "))
    if pilih == 1:
        many_rows = int(input("Berapa Data yang ingin di input "))
        i = 1
        while i <= many_rows:
            name = input("input nama barang = ")
            stock = int(input("input stock barang = "))
            price = int(input("input harga beli (dalam rupiah)= "))
            try:
                connection.insert_barang(name,stock,price)
            except:
                print("Data sudah ada ")
                break
                
            i = i+1
        print("data berhasil di input")    
        
    elif pilih == 2:
        nama_barang = input("pilih barang ")
        print(connection.tampil_barang(nama_barang))
 
 
def ui():
     st.title('Welcome')

st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

if __name__=='__main__':
    ui()
