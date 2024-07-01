# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:40:38 2024

@author: romouya
"""

'''
Edit this file to complete Exercise 5
'''

# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

# code up your solution here

#num_list = []
for i in range(1500,2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
       # num_list.append(i)
       # i += 1
#print(num_list)

    



# 2. Write a Python program to count the number of even and odd numbers from a series of numbers.

# example: numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# output:
# >>> Number of even numbers : 4
# >>> Number of odd numbers : 5

# code up your solution here

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_num = []
odd_num = [] 
for i in numbers:
    if i % 2 == 0 :
         even_num.append(i)
    else :
      odd_num.append(i)
print ('Number of even numbers:'+ str(len(even_num)))
print ('Number of odd numbers:' + str(len(odd_num)))
         
         


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
#out_put = []
for i in range(0,51):
    if i % 3 == 0 and i % 5 == 0:
       #out_put.append('fizzbuzz')
        print('fizzbuzz')
        
    elif i % 3 == 0:
        print ('fizz')
       # out_put.append('fizz')
    elif i % 5 == 0:
        print('buzz')
        #out_put.append('buzz')
        
    else:
        print(i)
       #out_put.append(i)
#print (out_put)





# 4. Given a list iterate it and display numbers which are divisible by 5 and if you find number greater than 150 stop the loop iteration

# examples: list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
# output:
# >>> 15
# >>> 55
# >>> 75
# >>> 150

# code up your solution here

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

#out_list1 = []
for i in list1:
    if i % 5 == 0 and i <= 150:
        print(i)
        #out_list1.append(i)
    elif i > 150:
        break
#print(out_list1)



# 5. Pick one of the questions above and use range() for a different solution

# code up your solution here

#4. using range()
#out_list2 = []
for i in range(201):
    if i % 5 == 0 and i <= 150:
        print(i)
        #out_list2.append(i)
   
        break
#print(out_list2)

# 6. Pick one of the question above and use comprehension for a different solution

# code up your solution here

#4. list comprehension

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

[i for i in list1 if i % 5 == 0 and i <= 150  ]



# 7. Pick one of the questions above and use while loop for a different solution

# code up your solution here

#1. while loop
i = 1500
while i <= 2700:
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    i += 1

'''
Edit this file to complete Exercise 6
'''

# def calculation(a, b):   
'''
	Write a function calculation() such that it can accept two variables 
	and calculate the addition and subtraction of it. 
	It must return both addition and subtraction in a single return call

	Expected output:
	res = calculation(40, 10)
	print(res)
	>>> (50, 30)

	Arguments:
	a: first number 
	b: second number

	Returns:
	sum: sum of two numbers
	diff: difference of two numbers
	'''

	# code up your solution here
def calculation(a, b):
    y = (a + b, a - b)
    return y

res = calculation(40,10)
print(res)

# def triangle_lambda():
	'''
	Return a lambda object that takes in a base and height of triangle
	and computes the area.

	Arguments:
	None

	Returns:
	lambda_triangle_area: the lambda
	'''
    def triangle_lambda():
        triangle_area = lambda x , y : x * y /2
        print (triangle_area(x=20,y=30))
    
    triangle_lambda()


    


#def sort_words(hyphen_str):
	'''
	Write a Python program that accepts a hyphen-separated sequence of words 
	as input, and prints the words in a hyphen-separated sequence after 
	sorting them alphabetically.

	Expected output:
	sort_words('green-red-yellow-black-white')
	>>> 'black-green-red-white-yellow'
	
	Arguments:
	hyphen_str: input string separated by hyphen

	Returns:
	sorted_str: string in a hyphen-separated sequence after 
	sorting them alphabetically
	'''

	# code up your solution here
   
    def sort_words(hyphen_str):
        words = hyphen_str.split('-')
        words.sort()
        sorted_words = "-".join(words)
        print(sorted_words)
   
  sort_words('green-red-yellow-black-white')
  

#def perfect_number():
	'''
	Write a Python function to check whether a number is perfect or not.

	A perfect number is a positive integer that is equal to the sum of 
	its proper positive divisors. Equivalently, a perfect number is a number 
	that is half the sum of all of its positive divisors (including itself).

	Example: 6 is a perfect number as 1+2+3=6. Also by the second definition,
	(1+2+3+6)/2=6. Next perfect number is 28=1+2+4+7+14. Next two perfect
	numbers are 496 and 8128.

	Argument:
	number: number to check

	Returns:
	perfect: boolean, True if number is perfect
	'''

	# code up your answer here
def perfect_number(num):
    sum_divisor = 0
    for i in range(1,num):
        if num % i == 0:
            sum_divisor += i
    return (sum_divisor + num)/2 == num

perfect_number(28)
            

if __name__ == '__main__':
	pass