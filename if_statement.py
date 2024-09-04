#nested if else
a=int(input("enter first number"))
b=int(input("enter 2nd number"))
c=int(input("enter 3rd number"))
print("you entered : ",a , b , c)
if(a>b and a>c):
    print("a is greater ")
else:
    if(b>c):
        print("b is greater")
    else:
        print("c is greater")        
