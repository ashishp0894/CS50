People = [
    {"name":"harry","House":"Gryffindor"},
    {"name":"Cho","House": "Ravenclow"}
]

def f(person): #short function
    return person["House"]

People.sort (key= lambda person:person["name"]) #using lamda
print(People)