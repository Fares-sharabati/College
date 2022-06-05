def main ():
    numbers = get_values()
    print("the numbers in the list are:")
    print(numbers)
def get_values():
    values= []
    again = "Y"
    while again.upper() == "Y":
        num = int(input("enter a number:"))
        values.append(num)
        print("do you want to add anthor number?")
        again = input("y = yes, anything else = no:")
        return values
main()
