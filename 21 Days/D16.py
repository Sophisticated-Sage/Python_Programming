print("loan calculator")

choice=int(input("enter your choice 1 (SI) or 2 (CI) : "))

if choice==1:
    p=eval(input("enter the value of p : "))
    r=eval(input("enter the value of r : "))
    t=int(input("enter the value of t : " ))
    si=p*r*t/100
    print(si)

if choice==2:
    p=eval(input("enter the value of p : "))
    r=eval(input("enter the value of r : "))
    t=int(input("enter the value of t : " ))
    n=eval(input("enter the value of n : "))
    ci=p*(1+r/n)*n*t
    print(ci)
