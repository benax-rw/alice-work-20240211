import os

os.system("clear")

print("Enter your name")
myInput = input(">>")
while(1):
   if not myInput:
      print("This field is mandatory!")
      myInput = input(">>")
   else:
      break;
print("You typed:",myInput)


