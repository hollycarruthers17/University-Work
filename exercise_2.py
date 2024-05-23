#1 Use a loop to find the numbers between 1500 and 2700 (both included) that are divisible by 7 and multiple of 5.

nl=[]
for x in range(1500, 2701):
    if (x%7 == 0) and (x%5 == 0):
        nl.append(str(x))
print(','.join(nl))



#2 Write a loop that prints the numbers in the Fibonacci series between 0 to 50.

x, y = 0, 1 

while y < 50:
    print(y)
    x,y = y, x+y


# 3 Construct a loop that prints the letter 'E' using the asterisk symbol.

result_str="";    
for row in range(0,7):    
    for column in range(0,7):     
        if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (row == 3 and column > 1 and column < 5)):  
            result_str = result_str + "*"    
        else:      
            result_str = result_str + " "    
    result_str = result_str + "\n"    
print(result_str)

