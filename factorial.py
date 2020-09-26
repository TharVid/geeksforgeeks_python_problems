#factorial
num=int(input("Enter a interger "))
result=1
for i in range(num):
    result+=(i*result)
print(result)