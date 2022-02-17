
#import built-in library for regular expressions
import re

#check list of regular expressions: d=digit from 0-9; s=single space
#UK Postcode in regular expressions: see https://ideal-postcodes.co.uk/guides/uk-postcode-format

#letter, letter/num, letter/number/space, letter/number/space, space, number, letter, letter 
#[A-Z]([A-Z]|[0-9])([A-Z]|[0-9]|[s])([A-Z]|[0-9]|[s])[s][0-9][A-Z][A-Z]


pattern = "^[A-Z]([A-Z]|[0-9]{1})([A-Z]|[0-9]{1}|[s])([A-Z]|[0-9]{1}|[s])[s][0-9]{1}[A-Z][A-Z]$"

#create a while loop - to enter various postcodes... 
Finished=False       
while not Finished:

    postcode=input("Please type your postcode: ")

#When the object is a string, the len() function returns the number of characters in the string.
#The == operator is a comparison operator in python compares values of two operands
    if len (postcode)== 0:
        Finished=True
    
    else:
    #use the re.match in the library
        if re.match(pattern, postcode):
            print("The post code is valid.")
        else: print("Try again. The post code is not valid.")



#Source: https://pythonschool.net/regular-expressions/python-and-regular-expressions/
#etc