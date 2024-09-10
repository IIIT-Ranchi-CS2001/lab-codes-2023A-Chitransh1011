# n = int(input("Enter the number : "))
#PROBLEM 1
# i = 1
# while i <= n:
#     print(i," -> ",i*i)
#     i = i+1

#PROBLEM 2
a = int(input("Enter the number : "))
sum = 0
while a>0:
    r = int(a%10)
    sum += r
    a = int(a/10)
print("Sum of digits : ",sum)

#PROBLEM 3
b = int(input("Enter the number : "))
count = 0
n1 = 0
n2 = 1
while count < b:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1

#PROBLEM 4
c = int(input("Enter the number : "))
d = int(input("Enter the limit  : "))
k = 1
for k in range(d):
      print(c," * ",k+1," = ",c*(k+1))
      k = k+1

#PROBLEM 5
s = input("Enter the string : ")
q = 0
for i in s:
      if i.isalnum()==0:
        q = 1
        break
if(q==0):
     print("String is alphanum")
else:
     print("String is not alphanum")

#PROBLEM 6
st =  input("Enter the string : ")
ch =  input("Enter the string : ")
r = 0
for char in st:
     if(ch==char):
          r += 1
print(r)
