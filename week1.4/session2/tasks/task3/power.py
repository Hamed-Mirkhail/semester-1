# Week 4, Session 2: Task 4

def power(x, n):
    # base case
    if n == 0:
        return 1

    # recursive case
    else:
        return x * power(x, n - 1)


# Test the function
print(power(2, 3))
print(power(5, 2))
print(power(3, 4))