


num=int(input("enter the number:-"))
n=num
ren=0
sum=0
while num>0:
    ren=num%10
    sum=sum+ren
    num=num//10
if n%sum==0:
    print(n,"is a harshad number")
else:
    print(n,"is not a harshad number")