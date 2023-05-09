import mysql.connector

mydb = mysql.connector.connect(
  host="192.168.0.105",
  user="fani",
  password="Happier1",
  database="fanidb"
)

mycursor = mydb.cursor()

print("\n")
company_n = input("Company: ")
number_of_empl = input("Number: ")
c_address = input("Address: ")
print("\n")

sql = "INSERT INTO companies (company_name, number_of_employees, address) VALUES (%s, %s, %s)"
val = (company_n, number_of_empl, c_address)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "Record Inserted.")
