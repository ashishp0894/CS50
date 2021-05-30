
'''
List is sequence of mutable [can be changed] values
Tuple is sequence of immutable values [can't be changed]
set is collection of unique values
dict is key value pairs
'''

name = "Harry"
print(name[0])
Characters = ["Harry","Ron","Hermoine"] #List with multiple elements
print(Characters)

List_Names = ["Harry","Ron","Hermoine","Ginnie"]
print(List_Names)
List_Names.append("Draco")
print(List_Names)
List_Names.sort()
print(List_Names)


Tuple_coordinate = (10.0,20.0) #Example of tuple - immutable list
print(Tuple_coordinate)



set_Names = set() #empty set
set_Names.add(1) #add elements
set_Names.add(2)
set_Names.add(4)
set_Names.add(3)
set_Names.add(3)
print(set_Names) #should print {1,2,3,4}

set_Names.remove(3) #remove any element
print(set_Names)
print(f"Total elements {len(set_Names)}") #len() prints length of stuff



houses = {"Harry":"Gryffindor","Draco":"Slytherin"} #Dictionary Created
print(houses["Harry"]) #Prints Gryffindor
houses["Hermoine"] = "Gryffindor" #Add new element

for i in houses:
    print(i)
