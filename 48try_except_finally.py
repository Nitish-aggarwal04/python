try:
  file = open('example.txt', 'r')
  content = file.read()
except FileNotFoundError:
   print("Error: The file was not found.")
finally:
   file.close()
print("Program is executed by Nitish 0231BCA017")
