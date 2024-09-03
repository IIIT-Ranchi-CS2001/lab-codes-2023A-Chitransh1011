#Question-1
s = "Maha Bharat"
x = s.swapcase()
print(x)
y = s.split()
print(y[1])
print(y[1]*3)
z = "Mera "
m = z+y[1]
print(m)
q = " Mahan"
w = z+y[1]+q
print(w)

#Question-2
a = "Ba Ba Black Sheep"
print(len(a))
print(a.find('e'))
print(a.count('a'))
b = a.split()
b[0] = "Ta"
b[1] = "Ta"
c = ' '.join(b)
print(c)