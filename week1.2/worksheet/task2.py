# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers

numbers = read_numbers ()

if len(numbers) == 0:
 sys.exitError("Error: no numbers provided")

minimum = min(numbers)
maximum = max(numbers)
numbers.sort()
mean = sum(numbers) / len(numbers)
med = len(numbers)
if med % 2 == 0:
 median = (numbers[med//2 - 1] + numbers[med //2]) / 2
else: 
 median = numbers[med // 2]

print (f"Minimum = {minimum}")
print (f"Maximum = {maximum}")
print (f"Mean = {mean}")
print (f"Median = {median}")