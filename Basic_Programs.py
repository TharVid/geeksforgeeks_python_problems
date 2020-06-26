#1
int1= float(input("Enter First Number"))
int2= float(input("Enter Secound Number"))
print(f"Sum is: {int1+int2}")

#2
int1= int(input("Enter a Number"))
def fact(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac

print(fact(int1))
#3
principle= float(input("Enter principle amount"))
#simple interest (P*T*R)/100
time= float(input("Time in year"))
rate= float(input("Rate"))
simple_interest= ((principle*time*rate)/100)

print(simple_interest)

#4
principle= float(input("Enter principle amount"))
#compound interest = P(1+R/100)**t
time= float(input("Time in year"))
rate= float(input("Rate"))
compound_interest = ((principle*(1+rate/100)**time))
print(compound_interest)

#5 (Importatnt)
int1= int(input("Enter number to check: "))
result=0
orig=int1
while int1>0:
    reminder=int1%10
    result= (result+(reminder*reminder*reminder))
    int1=int1//10
if orig== result:
    print("Armstrong")

else:
    print("Not armstrong")
#6
pi= 3.14
r= float(input("Enter Radious"))
area= pi*r*r
print(area)
#7


