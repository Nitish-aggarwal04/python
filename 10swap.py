#Using a Temporary Variable
a,b = 5,10

temp = a
a = b
b = temp

print("a =", a, "b =", b)

# Using Arithmetic: Addition & Subtraction
a,b = 5,10

a = a + b
b = a - b
a = a - b

print("a =", a, "b =", b)

#Using Multiplication & Division
a,b = 5,10

a = a * b
b = a / b
a = a / b

print("a =", int(a), "b =", int(b))

print("Program is executed by Nitish 0231BCA017")
