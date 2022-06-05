def main ():
    name_list = []
    again = "y"
    while again.upper() == "y":
        name = input("enter a name ")
        name_list.append(name)
        print("do you want to enter anthor name?")
        again = input("y = yes, anyhting else = no")
        print()
    print("here is the complete list")
    print(name_list)
main()
