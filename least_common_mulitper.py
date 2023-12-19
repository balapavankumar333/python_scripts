def Compute_LCM(n1,n2):
    if n1>n2:
        higher = n1
    else:
        higher=n2
    value=higher

    while True:
        if higher % n1 ==0 and higher%n2==0:
            print(" Lcm of ",n1 , "and",n2,"is",higher)
            break
        else:
            higher=higher+value

n1=int(input("ENter the first number :"))
n2=int(input("ENter the seconf  number :"))
Compute_LCM(n1,n2)