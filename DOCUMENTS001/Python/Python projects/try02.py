sum = 0
non=0
again = 'y'
while again == 'y':
    number= int(input("enter an integer  number: "))
    again=input('eter y to enter anthor number:')
    sum=sum+number
    non=non+1
print(sum)
print(sum/non)
