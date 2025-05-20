import mysql.connector
import datetime

db= mysql.connector.connect(
    host = "0-igg.h.filess.io",
    database = "storage_costtownon",
    port = "61002",
    username = "storage_costtownon",
    password = "c06342c974f010f014d095af8ebf435cbfd5beca"
)
if db.is_connected() is True:
    print("Connected!")
else:
    print("Not Connected")
 



 

def insert_barang(nama,stock,harga):
    creation_dates=  datetime.datetime.now()
    creation_date_format = creation_dates.strftime('%Y-%m-%d %H:%M:%S')
    cursor = db.cursor()
    cek = cursor.execute("select 1 from storage where name = %s",(nama,))
    if cek:
        insert = cursor.execute("INSERT INTO storage (name,stock,price,creation_date) values (%s,%s,%s,%s)",(nama,stock,harga,creation_date_format))
        db.commit()  
      
    return insert

def tampil_barang(nama):
    cursor = db.cursor()
    write = cursor.execute("select * From storage where name = IFNULL(%s,name)",(nama,))
    result = cursor.fetchall()
    
    return result