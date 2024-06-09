'''
Edit this file to complete Exercise 6
'''

def calculation(a, b):
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
    return a+b, a-b


def triangle_lambda():
    '''
    Return a lambda object that takes in a base and height of triangle
    and computes the area.

    Arguments:
    None

    Returns:
    lambda_triangle_area: the lambda
    '''

    lambda_triangle_area = lambda b,h: b*h/2
    return lambda_triangle_area


def sort_words(hyphen_str):
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
    sorted_str = '-'.join(sorted(hyphen_str.split('-')))
    return sorted_str


def perfect_number(number):
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
    divisor_sum = 0
    for i in range(1, number):
        if number%i == 0:
            divisor_sum += i

    if divisor_sum == number:
        perfect = True
    else:
        perfect = False

    return perfect


if __name__ == '__main__':
    pass