import sys
try:
    x = int(input("X:"))
except ValueError:
    print ("enter correct value")
    sys.exit(1)

y = int(input("Y:"))


try :
    result = x/y
except ZeroDivisionError:
    print("Can't divide by 0")
    sys.exit(1)
print (f"X/Y is {x/y}")