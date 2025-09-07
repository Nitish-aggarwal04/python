try:
   number = int(input("Enter a number: "))
   result = 10 / number
except ZeroDivisionError:
   print("Error: Cannot divide by zero.")
else:
   print(f"The result is {result}.")
print("Program is executed by Nitish 0231BCA017")
