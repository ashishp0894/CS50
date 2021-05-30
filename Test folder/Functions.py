def Square_number(Number_to_Square): #Defining a function
    return Number_to_Square*Number_to_Square

Number_to_Square = int(input("Enter Number till square needed: "))
#print(Square_number(Number_to_Square))

for i in range(1,Number_to_Square):
    print(f"Square of {i} is {Square_number(i)}")

