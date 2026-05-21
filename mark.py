print("marksheet calculation")
a=float(input("enter tamil mark:"))
b=float(input("enter english mark:"))
c=float(input("enter maths mark:"))
d=float(input("enter science mark:"))
e=float(input("enter social mark:"))
total=a+b+c+d+e
print("total marks:",total)
average=total/5
print("average marks:",average)
if(a>=35 and b>=35 and c>=35 and d>=35 and e>=35):
    print("pass")
else:
    print("fail")
   
