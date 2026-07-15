num=int(input("Enter the number: "))
if(num<1):
    print("Please enter a postive number")
else:
    if num%2==0:
        print(num,"is a even number",end=" ")
    else:
        print(num,"is a odd number",end=" ")
    if num==1:
        print("is not a prime number")
    else:
        flag=0
        for i in range(2,num//2):
            if num%i==0:
                flag=1
                break
        if flag==1:
            print("and is not a prime number")
        else:
            print("and is a prime number")