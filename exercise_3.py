#1. Write a function that generates a random password:
#   The password should have a random length of between 7 and 10 characters. 
#   Each character should be randomly selected from (the decimal)positions 33 to 126 in the ASCII table. 
#   Your function will not take any parameters. 
#   It will return the randomly generated password as its only result. 
#   Hint: You will need to use the chr function for this exercise. 

from random import randint

shortest = 7
longest = 10
min_ascii = 33
max_ascii = 126

def random_password():
    random_length = randint(shortest, longest)
    result = ""
    for i in range(random_length):
        random_char = chr(randint(min_ascii, max_ascii))
        result      = result + random_char
    return result 

def main():
    print("Your random password is:",random_password())

main()


#2. Use the sorted() function and a lambda function to sort the words in the list based on their second letter from a to z.
#   lst=["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst = ["otter", "whale", "goose", "chipmunk", "fox", "sheep", "rabbit", "marten"]

lst = sorted(lst, key=lambda x: x[0])

print(lst)