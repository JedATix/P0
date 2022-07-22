

#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
import pythonql
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    L = S.split(':')
    St = ""
    if L[2][2] =="P" and int(L[0])<12:
        St = str (int(L[0])+12) + ":" +L[1]+":"+L[2][1]+L[2][2]
    else:
        St = str (int(L[0])) + ":" +L[1]+":"+L[2][0]+L[2][1]
    return St

    


date_string = '2009-11-29 03:17 PM'
format = '%Y-%m-%d %H:%M %p'
my_date = datetime.strptime(date_string, format)

# This prints '2009-11-29 03:17 AM'
print (my_date.strftime(format))


import json

# Define json data
customerData ="""{
    "id": "3425678",
    "name": "John Micheal",
    "email": "john@gmail.com",
    "type": "regular",
    "address": "4258 Poplar Chase Lane, Boise, Idaho."
}"""

# Input the key value that you want to search
keyVal = input("Enter a key value: \n")

# load the json data
customer = json.loads(customerData)
# Search the key value using 'in' operator
if keyVal in customer:
    # Print the success message and the value of the key
    print("%s is found in JSON data" %keyVal)
    print("The value of", keyVal,"is", customer[keyVal])
else:
    # Print the message if the value does not exist
    print("%s is not found in JSON data" %keyVal)


