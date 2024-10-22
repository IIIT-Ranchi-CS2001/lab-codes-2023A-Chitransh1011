#Ques-1
s = "bob eats apple"
count = 0
for i in s: 
    print(i)
    t = i[::-1]
    print(t)
    if(i==t):
        count+=1
print(count)

#Ques-2
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
print("List of numbers:", numbers)
# Calculate mean
mean = sum(numbers) / len(numbers)
print("Mean:", mean)
# Calculate median
numbers.sort()
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2
else:
    median = numbers[n//2]
print("Median:", median)
# Calculate mode
frequency = {}
for i in numbers:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

max_freq = max(frequency.values())
modes = [key for key, value in frequency.items() if value == max_freq]
print("Mode:", modes)

#Ques-3
course_codes = ["CS1001", "CS1002", "CS1003"]
course_names = ["Python", "Data Structures", "Algorithms"]
combined_courses = [f"{code}:{name}" for code, name in zip(course_codes, course_names)]
print(combined_courses)

#Ques-4
students = ["Rohit", "Virat", "Risabh", "Sachin", "Kapil", "Shubam"]
singers = {student for student in students if student in ["Rohit", "Risabh", "Kapil"]}
dancers = {student for student in students if student in ["Virat", "Risabh", "Sachin"]}
all_artists = singers | dancers
print("All artists:", all_artists)
allrounders = singers & dancers
print("All rounders:", allrounders)
dancers_not_singers = dancers - singers
print("Dancers but not singers:", dancers_not_singers)
singers_not_dancers = singers - dancers
print("Singers but not dancers:", singers_not_dancers)
exclusive_artists = dancers ^ singers
print("Dancers but not singers cum singers but not dancers:", exclusive_artists)

