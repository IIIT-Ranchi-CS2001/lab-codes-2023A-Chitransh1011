#Question-3
# a = input("Enter a string : ")
# b = a[::-1]
# if(a==b):
#     print("It is a Palindrome.")
# else:
#     print("Not a Palindrome.")

#Question-4
name = input("Enter a Name : ")
rollno = int(input("Enter a RollNo : "))
marks = int(input("Enter a Marks : "))
g = 0
remarks = ""

if(marks>=90):
    g = 10
    remarks += "OUTSTANDING"
elif(marks<90 and marks>=80):
    g = 9
    remarks += "VERY GOOD"
elif(marks<80 and marks>=70):
    g = 8
    remarks += "GOOD"
elif(marks<70 and marks>=60):
    g = 7
    remarks += "AVERAGE"
elif(marks<60 and marks>=50):
    g = 6
    remarks += "PASS"
else:
    g = 0
    remarks += "FAIL"

print("NAME : ",name," , GRADE POINT : ",g," , REMARKS : ",remarks)