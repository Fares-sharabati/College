def main():
    x = str(input("enter a string for ssn (ddd-dd-dddd): "))
    if len(x)==9:
        print("valid ssn")
    else:
        print("invalid ssn")
main()
