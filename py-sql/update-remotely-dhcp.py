from os import system,popen
import mysql.connector

print("Resolving the IP of the DB Host...")
mhost = popen("nmap -v -sn 192.168.0.0/24 >/dev/null && arp -an | grep b8:27:eb:47:6c:36 | awk '{print $2}' | sed 's/[()]//g'").read()
print("DB Host IP found:", mhost)
print("Now updating data...")
mydb = mysql.connector.connect(
  host=mhost,
  user="fani",
  password="Happier1",
  database="fanidb"
)

mycursor = mydb.cursor()
sql = "UPDATE companies SET address = 'Rubavu City' WHERE id = 1"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")
