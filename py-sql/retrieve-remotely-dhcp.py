from os import system,popen
import mysql.connector

print("Resolving the IP of the server...")
mhost = popen("nmap -v -sn 192.168.0.0/24 >/dev/null && arp -an | grep b8:27:eb:47:6c:36 | awk '{print $2}' | sed 's/[()]//g'").read()


mydb = mysql.connector.connect(
  host=mhost,
  user="fani",
  password="Happier1",
  database="fanidb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM companies")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
