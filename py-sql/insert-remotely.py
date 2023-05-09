import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.105",
  user="fani",
  password="Happier1",
  database="fanidb"
)

mycursor = mydb.cursor()

sql = "INSERT INTO companies (company_name, number_of_employees) VALUES (%s, %s)"
val = ("DELL", "2208")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Record Inserted.")