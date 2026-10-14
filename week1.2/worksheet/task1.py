# Worksheet 1.2: Task 1 Solution
import sys

try:
 integer = int(input("enter grade: "))
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")

if (integer) < 0 or (integer) > 100:
 sys.exit("Error: Grade must be an integer between 0 and 100")
elif (integer) <= 39:
 print(f"{integer} is a Fail")
elif (integer) >= 40 and (integer) < 70:
 print (f"{integer} is a Pass") 
else:
 print (f"{integer} is a Distinction")


