def main():
    total=0
    n=int(input("enter a nonneative integer:"))
    for x in range(1,n,+1):
        total*=x
    print(total)
main()
