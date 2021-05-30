""" Function that takes function as input and can create it's modified version"""

def announce (f):
    def wrapper():
        print ("About to run the function:")
        f()
        print ("Done")
    return wrapper

@announce #Leads to change in capablity of hello function ex: to check if user is logged in always before any function
def hello ():
    print("Hello world")

hello()

