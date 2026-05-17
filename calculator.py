
from random import choice


print("1 addition")
print("2 subtraction")
print("3 multiplication")
print("4 division")
print("5 power")

choice=input("enter your choice:")


val1= int(input('enter the value1:'))
val2= int(input("enter the value2:"))

if choice == 1:
  print(val1+val2)
elif choice == 2:
    print(val1-val2)
elif choice == 3:
    print(val1*val2)
elif choice == 4:
    print(val1/val2)
elif choice == 5:
    print(val1**val2)
else :
    print("not valid input,command terminated")
