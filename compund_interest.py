#compound intrest A = P(1 + R/100) t
principal=float(input("Enter Proncipal Amount "))
rate=float(input("Enter Annual Rate "))
time= float(input("Enter time in years "))
final_amount= float (principal*(1+((rate/100)*time)))
print(final_amount)