x = 6
y = 0

a = 0
b = 3

#sentencia if
if x == 6:
    y = 5
else:
    y = 2

print(y) #5

#sentencia elif
if x == 4:
    y=1
elif x == 5:
    y=2
elif x == 6:
    y = 3
else:
    y = 3

print(y) #3

#ciclo for
for x in range(1, 10):
    print(x) # 1 a 9

#ciclo while
while a < b:
    print(a)
    a += 1 # 0  1  2

#sentencia while
while a < b:
    print(a)
    a += 1 # incrementa

    if a == 2:
        break
    else:
        print("condicional") # 0  condicional  1

# sentencia continue
for i in range(1, 10):
    if i % 2 != 0:
        continue
    print(i) # 2  4  6  8

