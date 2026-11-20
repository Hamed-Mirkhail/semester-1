# Week 4, Session 2: Task 1
import calendar

print(calendar.month(2025, 10))

# Two more month function calls with different w and l values
print(calendar.month(2025, 10, w=4, l=2))

print(calendar.month(2025, 10, w=6, l=3))


# Three calendar function calls with different optional arguments

print(calendar.calendar(2025, w=4, l=2, c=8, m=3))

print(calendar.calendar(2025, w=2, l=1, c=4, m=4))

print(calendar.calendar(2025, w=3, l=2, c=10, m=2))