#1
print('Hello World')

#2
print('Hello, world') 
user_name = input('Enter your name: ') 
print('Hello ', user_name)

#3
print('Hello, world')
name = input('Enter your name: ') 
print('Hello', name) 
name = input('What is the name of your best friend: ') 
print('Hello Best Friend', name)

#4
my_variable = 'John' 
print(my_variable) 

my_variable = 42
print(my_variable)

my_variable = True 
print(my_variable)


#5: Comments in code
#This is a comment 
name = input('Enter your name: ') 

#This is another comment 
print(name)	#this is a comment to the end of the line

#6: Variable Types
#Strings
my_variable = 'Bob' 
print(type(my_variable))

#6: Working with strings
#Concatenation
string_1 = 'Good' 
string_2 = " day" 
string_3 = string_1 + string_2 

print(string_3) 

print('Hello ' + 'World')

#7: Working with strings
#Concatenation
string_1 = 'Good' 
string_2 = " day" 
string_3 = string_1 + string_2 

print(len(string_3))

#7: Working with strings
#Accessing a Character
my_string = 'Hello World' 
print(my_string[4])

#7: Working with strings
#Accessing a Character
my_string = 'Hello World' 
print(my_string[4])

#7: Working with strings
#Accessing a Subset of Characters
my_string = 'Hello World' 

print(my_string[4])                #characters at position 4 
print(my_string[0:5])              #from start to position 5
print(my_string[2:len(my_string)]) #from position 2 to the end


#8: Working with strings
#Repeating Strings
print('*' * 10) 
print('Hi' * 10)

#9: Working with strings
#Splitting Strings
title = 'The Good, The Bad, and the Ugly' 
print('Source string:', title)
print('Split using a space') 
print(title.split(' ')) 
print('Split using a comma') 
print(title.split(','))

#9: Working with strings
#Counting Strings
my_string = 'Count, the number of spaces' 
print("my_string.count(' '):", my_string.count(' '))

#9: Working with strings
#Replacing Strings
welcome_message = 'Hello World!' 
print(welcome_message.replace("Hello", "Goodbye"))

#9: Working with strings
#Converting Other Types into Strings
#Error
#msg = 'Hello Lloyd you are ' + 21
#print(msg)
#Fine
msg = 'Hello Lloyd you are ' + str(21)
print(msg)

#9: Working with strings
#String Formatting
name = "Adam" 
age  = 20 
print("{} is {} years old".format(name, age)) 

#9: Working with strings
#String Formatting
#Can specify an index for the substitution 
format_string = "Hello {1} {0}, you got {2}%" 
print(format_string.format('Smith', 'Carol', 75))

#9: Working with strings
#String Formatting
#named values for the placeholders
format_string = "{artist} sang {song} in {year}" 
print(format_string.format(artist='Paloma Faith', song='Guilty', year=2017))

#10: Converting Between Types
int_value    = 1
string_value = '1.5' 
float_value  = float(int_value) 

print('int value as a float:', float_value) 
print(type(float_value)) 

float_value = float(string_value) 
print('string value as a float:', float_value) 
print(type(float_value))

#11: Boolean Values
all_ok = True 
print(all_ok) 

all_ok = False 
print(all_ok) 

print(type(all_ok))

#11: Boolean Values
#Converting to Integers
print(int(True)) 

print(int(False)) 

print(bool(1)) 

print(bool(0))

#12: Assignment Operators
x = 0 
x += 1 # has the same behaviour as x = x + 1
print(x)

#13: None Value
winner = None 
print('winner:', winner) 
print('winner is None:', winner is None) 
print('winner is not None:', winner is not None) 
print(type(winner)) 
print('Set winner to True') 

winner = True 
print('winner:', winner) 
print('winner is None:', winner is None) 
print('winner is not None:', winner is not None) 
print(type(winner))