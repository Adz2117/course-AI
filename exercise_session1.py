#first
#star triangle
print("first :")
a = int(input("please add your arbitrary number : "))
b = a-1
c = 1
while a > 0:
    print(" " * b, "*" * c)
    a = a - 1
    b = b - 1
    c = c + 2
print("\n")
print("end \n")

#second
#get a number from user and determine that is prime number or not
print("second :")
a = int(input("please add your arbitrary number to determine that is prime number or not : "))
b = 0
for i in range( 1 , a+1):
    if a%i == 0:
        b += 1

if b == 2:
    print(f"{a} , yes it is a prime number.")
else:
    print(f"{a} , no it isn't a prime number.")
print("\n")
print("end \n")

#third
#determine prime number until 1000
print("third :")
for i in range(1 , 1001):
    if i > 1:
        for c in range(2 , i):
            if i % c == 0:
               break
        else:
            print(i)