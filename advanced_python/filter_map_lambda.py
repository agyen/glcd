def is_even(x):
    if x%2 == 0:
        print("true")
    elif x%2 != 0:
        print("false")
              
              
is_even(2)


# returning even numbers from a list
def is_even(l):
    enum = []
    for n in l:
        if n%2 == 0:
            enum.append(n)
    return enum


x = is_even([1,56,234,87,4,76,24,69,90,135])
print(x)

#returning even numbers from a list using lamba

numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
even_numbers = list(filter(lambda x: x%2 == 0,numbers))
print(even_numbers)

#returning odd numbers
numbers = [1, 56, 234, 87, 4, 76, 24, 69, 90, 135]
even_numbers = list(filter(lambda x: x%2 != 0,numbers))
print(even_numbers)   
    



