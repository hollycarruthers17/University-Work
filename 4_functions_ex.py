#Print Message 1
#from matplotlib.dates import num2date


def print_msg(): 
    print('Hello World!')

print_msg()

#Print Message 2
def print_my_msg(msg):
    print(msg)

print_my_msg("Hello")

#Returning Values
def square(n):
    return n*n

square(3)

#Docstrings
def do_calculations(n1): 
    """This function takes a number as parameter and computes two results:
    *The first result is the number squared
    *The second result is the number plus 5"""
    res1 = n1*n1
    res2 = n1 + 5
    return res1,res2

do_calculations(2)
r1,r2 = do_calculations(2)
r1

#Multiple Parameter Functions
def do_calculations(n1,n2): 
    res1 = n1*n2
    res2 = n1 + n2 + 5
    return res1,res2

#Named Arguments
def greeter(name,
            title = 'Dr',
            prompt = 'Welcome',
            message = 'Live Long and Prosper'): 
    print(prompt, title, name, '-', message)
    
greeter(name = 'Nacho') 
greeter(message = 'We like Python', name = 'Nacho')

#Arbitrary Arguments
def greeter(*args):
    for name in args: 
        print('Welcome', name)
        
greeter('John', 'Denise', 'Phoebe', 'Adam', 'Gryff', 'Jasmine')

#Positional and Keyword Arguments 1
def my_function(*args,**kwargs): 
    for arg in args: 
        print('arg:', arg) 
    for key in kwargs.keys(): 
        print('key:', key, 'has value: ', kwargs[key])
        
my_function('John', 'Denise', daughter='Phoebe', son='Adam')
print('-' * 50) 
my_function('Paul', 'Fiona', son_number_one='Andrew', son_number_two='James', daughter='Joselyn')

#Positional and Keyword Arguments 2
def named(**kwargs): 
    for key in kwargs.keys(): 
        print('arg:', key, 'has value:', kwargs[key]) 

named(a=1, b=2, c=3)

#Anonymous Functions
double = lambda i: i*i

double(10)
print(double(10))



#*********************************************************************************************************
#Python Functions from YouTube

def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome Aboard")


greet('Holly','Carruthers')
greet('John', 'Smith')

def greet(name):
    print(f'Hi{name}')

def get_greeting(name):
    return f"Hi{name}"

message = get_greeting("Mosh")


#Keyword Arguement 
def increment(number, by):
    return number + by

result = increment(2,1)
print(result)

print(increment(2, by=1))


def increment(number, by=1):        #all optional paramters come last
    return number + by

print(increment(2, 5))


#Args           
#square brackets to create lists; parentheses to create tuples

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number 
    return total 

print(multiply(2, 3, 4, 5)) 

#Dictionaries                       #multiple keyword arguements
def save_user(**user):
    print(user["name"])

save_user(id=1, name="John", age=22)


#Scope 
message = 'a' 
                                    
def greet(name):
    message = 'b'

greet("Mosh")
print("message")