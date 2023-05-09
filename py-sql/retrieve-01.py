from os import system,popen
import mysql.connector

system("clear")

f=open("mhost.txt")
mhost=f.read()

#print("Resolving the IP of the server...")
#mhost = popen("nmap -v -sn 192.168.0.0/24 >/dev/null && arp -an | grep b8:27:eb:47:6c:36 | awk '{print $2}' | sed 's/[()]//g'").read()

f.write(mhost)
f.close()

print("Server IP is", mhost)

mydb = mysql.connector.connect(
  host=mhost,
  user="fani",
  password="Happier1",
  database="fanidb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM companies")

if mycursor.rowcount == 0:
    print('No rows to return!')
else:
    rows = mycursor.fetchall()

    for row in mycursor:
      company_name = row
      print("%s",company_name)
