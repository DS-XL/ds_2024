'''
Edit this file to complete Exercise 5
'''

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here
rst = []
for i in range(1500, 2701):
	if i % 7 == 0 and i % 5 == 0:
		rst.append(i)
print(rst)

# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here
# code up your solution here
import random

numbers = [random.randint(-100, 100) for i in range(10)]
counts = {'even': 0, 'odd': 0}

for i in numbers:
    match i % 2:
        case 0:
            counts['even'] += 1
        case 1:
            counts['odd'] += 1
        case _:
            print(f'{i} is not an integer')
print(f'Number of even numbers: {counts["even"]}')
print(f'Number of odd numbers: {counts["odd"]}')

# 3. Write a Python program which iterates the integers from 0 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

# Expected Output :
# >>> fizzbuzz
# >>> 1
# >>> 2
# >>> fizz
# >>> 4
# >>> buzz
# >>> ...

# code up your solution here
i = 0
while i<=50:
    if i % 3 == 0:
        match i % 5:
            case 0:
                print('fizzbuzz')
            case _:
                print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)
    i += 1

# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here
i, list1 = 0, [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
while list1[i] <= 150:
    if list1[i] % 5 == 0:
        print(list1[i])
    i += 1

# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here
## refactoring problem 3
for i in range(0,51):
    if i % 3 == 0:
        match i % 5:
            case 0:
                print('fizzbuzz')
            case _:
                print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(i)

# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here
# refactoring problem 4
print([x for x in list1 if x % 5 == 0 and x <= 150])

# 7. Pcik one of the questions above and use while loop for a different solution

# code up your solution here
# refactoring problem 1
i, rst = 1500, []
while i < 2701:
    if i % 7 == 0 and i % 5 == 0:
        rst.append(i)
    i += 1
print(rst)