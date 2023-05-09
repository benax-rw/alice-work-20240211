import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.105",
  user="fani",
  password="Happier1",
  database="fanidb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM companies")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
