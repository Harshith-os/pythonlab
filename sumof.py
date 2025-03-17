
n = int(input("Enter the number up to which you want to sum odd numbers: "))
s = 0
i = 1


while i <= n:
    s += i
    i += 2 
print("Sum of odd numbers up to", n, "is:", s)
