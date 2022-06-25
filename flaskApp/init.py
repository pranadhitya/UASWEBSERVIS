import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="prana",
  passwd="prana123",
  db= "web"
)

if db.is_connected():
  print("Berhasil terhubung ke database")