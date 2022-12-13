a=int(input("enter the starting of the range: "))
b=int(input("enter the ending of the range: "))
c=0
d=0
if b>1:
    for i in range(a,b+1):
        if i > 1:
            for j in range(2, int((i / 2) + 1)):
                if i % j == 0:
                    print(i, "is a composite number")
                    c = c + 1
                    break
            else:
                print(i, "is a prime number")
                d=d+1
        else:
            print(i, "is a composite number")
            c=c+1
print(d,"prime and",c,"composite numbers in the range")
