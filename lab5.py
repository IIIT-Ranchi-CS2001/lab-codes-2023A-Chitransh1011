#PROBLEM I Generate two tuples to represent two distinct points in space. (Three dimensional geometry). Determine the Euclidean distance between the two.
t1 = tuple(map(int, input("Enter the coordinates of the first point (x1, y1, z1) separated by spaces: ").split()))
t2 = tuple(map(int, input("Enter the coordinates of the second point (x2, y2, z2) separated by spaces: ").split()))
a = (t1[0] - t2[0])**2 + (t1[1] - t2[1])**2 + (t1[2] - t2[2])**2
b = a**0.5
print(f"The Euclidean distance between {t1} and {t2} is {b}")

#PROBLEM 2 Enter the coordinates of two points on the cartesian plane (take user input using comprehension). Find the equation of the straight line passing through these points.
x1, y1 = [int(i) for i in input("Enter the coordinates of the first point (x1, y1) separated by a space: ").split()]
x2, y2 = [int(i) for i in input("Enter the coordinates of the second point (x2, y2) separated by a space: ").split()]
if x1 == x2:
    print(f"The line is vertical with equation: x = {x1}")
else:
    m = (y2 - y1) / (x2 - x1)
    c = y1 - m * x1 
    print(f"The equation of the line is: y = {m}x + {c}")

#PROBLEM 3 WAP to count the number of each character present in a string using the concept of a dictionary.
string = input("Enter a string: ")
cnt = {}
for char in string:
    if char in cnt:
        cnt[char] += 1
    else:
        cnt[char] = 1

print(cnt)

#PROBLEM 4 Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. Construct a list of tuples with and without using built-in function zip()
names = [input("Enter customer names separated by spaces: ").split()]
ids = [input("Enter customer IDs separated by spaces: ").split()]
points = [input("Enter shopping points separated by spaces: ").split()]
# Using zip
a = list(zip(names, ids, points))
print(a)
#Without zip
b = [(names[i], ids[i], points[i]) for i in range(len(names))]
print(b)

#PROBLEM 5 Sort the list of tuples constructed above with and without sorted function. 
#With sorted
sorted_data = sorted(a, key=lambda x: x[2])
print("Sorted using sorted():", sorted_data)
#without Sorted
n = len(a)
for i in range(n):
    for j in range(0, n-i-1):
        if a[j][2] > a[j+1][2]:  # Comparing shopping points (index 2)
            a[j], a[j+1] = a[j+1], a[j]

print("Sorted without sorted() :", a)