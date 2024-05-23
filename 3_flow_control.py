#A basic IF statement
num = int(input('Enter a number: '))
if num < 0:
  print(num, 'is negative')


#Adding a bit of complexity
num = int(input('Enter another number: ')) 
if num > 0: 
  print(num, 'is positive') 
  print(num, 'squared is ', num * num) 
print('Bye')
 
#A basic if-else statement
num = int(input('Enter yet another number: ')) 
if num < 0: 
  print('Its negative') 
else: 
  print('Its not negative')
 

#A basic if-elif-else statement
savings = float(input("Enter how much you have in savings: ")) 

if savings == 0: 
  print("Sorry no savings") 
elif savings < 500: 
  print('Well done') 
elif savings < 1000: 
  print('Thats a tidy sum') 
elif savings < 10000: 
  print('Welcome Sir!') 
else: 
  print('Thank you')

#A basic IF expression
age    = 15 
status = None 

if (age > 12) and age < 20:
  status = 'teenager' 
else: 
  status = 'not teenager' 
print(status)


#A basic WHILE loop
count = 0
print('Starting')
while count < 100:
  print(count,' ',end='')	  #part of the while loop
  count += 1                #also part of the while loop
print("Done")               #Not part of the while loop

#A basic FOR loop
#Loop over a set of values in a range 
print('Print out values in a range') 
for i in range(0,10):
  print(i)
print() 
print('Done')

#Now use an 'anonymous' loop variable 
for _ in range(0,10):
  print('.', end='')
print()

#Breaking a loop
print('Only print code if all iterations completed') 
num = int(input('Enter a number to check for: ')) 

for i in range(0, 6): 
  if i == num:
    break
  print(i, ' ', end='') 
print('Done')

#Continuing a loop
for i in range(0, 10):
  print(i, ' ', end='')
  if i % 2 == 1:
    continue 
  print('hey its an even number') 
  print('we love even numbers') 
print('Done')