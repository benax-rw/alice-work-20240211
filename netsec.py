from os import system,popen
import urllib.parse
import json,urllib.request
import sys
x = urllib.request.urlopen("http://192.168.0.87/Y3-Exam-Term1-2021~2022/?rq=get-netsec-exam-16dec2021-questions").read()
y = json.loads(x)
system("clear")
print("Rwanda Coding Academy (RCA)")
print("End-Term-1 Exam | Y-3")
print("Course Title: Network Security")
print("Date: 2021-12-16")
print("Duration : 2 hours")
print("Total: 30 marks")
print("Good New: Having arrived here you already have 10 marks")
print("=================================\n")
def isListed(st):
    print("Verifying...")
    result = popen("curl --request POST --form student_id="+st+" http://192.168.0.87/Y3-Exam-Term1-2021~2022/?rq=verify").read()
    if("Welcome" in result):
        print("\n*****************************************\n")
        print(result)
        print("\n*****************************************\n")
        return "Listed"
    else:
        return "Unlisted"
    print("\n")
def saveAnswer(arg,n, flag):
    print("Saving Answer-"+n+"...")
    cmd="curl --request POST --form flag="+flag+"  --form  student_id="+student_id+" --form  answer="+arg+" http://192.168.0.87/Y3-Exam-Term1-2021~2022/?rq=insert"
    system(cmd)
    print("+++++++++++++++++++++++++++++++++++")
    print("\n")
print("Enter your ID: [in the format rca03****]")
student_id = input(">>")
if(student_id==""):
    print("This field can't be left empty")
    student_id = input(">>")
else:
    if(isListed(student_id)=="Listed"):
        while True:
            print("Read every line of the code below and then answer ensuing questions.\n")
            f = open("script-202112151240.cpp", "r")
            print(f.read())
            print("\n")
            for k in range(len(y)):
                if(k<(len(y)-1)):
                    flag = "0" #flag 0 means work in progress
                else:
                    flag = "1" #flag 1 means work completed
                print("Question-"+y[k]["id"]+":")
                print(y[k]["question"])
                
                
                answer = input("Answer-"+y[k]["id"]+":")
                while(1):
                   if not answer:
                      print("Please don't skip this question!")
                      answer = input("Answer-"+y[k]["id"]+":")
                   else:
                      break;
                answer=urllib.parse.quote(answer)
                saveAnswer(answer, y[k]["id"],flag)
            break
    else:
        print("\nOOPS!\nThe student ID you entered does not match with any candidate!\n")
