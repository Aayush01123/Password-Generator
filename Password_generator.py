#Python Program To Create A Random Password Generator
# Batch32
# Section A
# Name: Aayush Tiruwa

#import the necessary modules!
import random
import string

print("Welcome to our Random Password Generator")

def main():
    
    #input the length of the password
    length = int(input("Enter the length of password you want: "))

    #define data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbols = string.punctuation

    #combine the data
    combine = lower + upper + digit + symbols

    #use random
    x = random.sample(combine, length)

    #Create the password
    password = "".join(x)

    #print the password
    print("Your Password is : ", password)
    main()

main()

