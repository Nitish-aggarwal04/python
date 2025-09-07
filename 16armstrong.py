n = int(input("Enter number: "))
power = len(str(n))
total = sum(int(digit) ** power for digit in str(n))

if total == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")
