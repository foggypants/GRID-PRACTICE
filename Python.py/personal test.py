a=input("Enter your name: ")
roll=int(input("Enter your Roll no.: "))
b=int(input("Enter your Maths marks: "))
c=int(input("Enter your Science marks: "))
d=int(input("Enter you English marks: "))
sum=b+c+d
avg=sum/3
print("-----------STUDENT REPORT CARD----------")
print("Name   : ",a)
print("Rollno : ",roll)
print("Total  : ",sum)
print("Average: ",avg)
if avg>35:
    print("RESULT:PASS")
else:
    print("RESULT:FAIL")
print("------------------------------------------")