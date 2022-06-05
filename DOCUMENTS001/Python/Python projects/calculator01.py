print("Welcome to the calculator")
print("select an operation to perform:")
print("1. ADD")
print("2. SUBTRACT")
print("3. DIVIDE")
print("4. MULTIPLY")

operation =input("choose an operation to kepp going ")
total =0
x = int(input("enter how many number you want to calculate:"))

if operation == "1":
    for i in range(x):
        num=float(input("enter a number"))
        total+=num
    print(total)
elif operation == "2":
    for i in range (x):
        num=float(input("enter a number"))
        total-=num
    print(total)
elif operation == "3":
    num1 = input("Enter Number 1:")
    num2 = input("Enter Number 2:")
    print("Total is" + str(int(num1) / int(num2)))
elif operation == "4":
    for i in range (x):
        num=float(input("enter a number"))
        total*=num
    print(total)
else :
    print("invalid")
