# Exercise 2

# 2.1
numerator = 123
denominator = 456

# code up your solution below
print(str(numerator)+'/'+str(denominator)+' = '+str(round(numerator/denominator,8)))
# a bit cleaner
print('{0}/{1} = {2:.8f}'.format(numerator, denominator, numerator/denominator))

# 2.2
# code up you solution here
ds = "Data Science"
print(ds[::2])

# what if the string is the one that starts and ends with quotations?
ds = '"Data Science"'
print(ds)
print(ds[::2])

# 2.3
regex_wiki.lower().replace(' ','')

# 2.4
modified = data_science.replace('data', '<3')
print(modified)
print('\n')
print('data' in modified)

# 2.5
re.sub(r'(?<=(?i)d)(a)(?=ta )', '<3', data_science, re.IGNORECASE)

aaa = 'DATA Data DaTA dATA dota daTa'
re.sub(r'(?<=(?i)d)(a)(?=(?i)ta )', '<3', aaa)


# exercise 3

# 3.1
score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
    
print(grade)

# 3.2
x = 1
y = 1

if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x is the same as y')


# exercise 4

# 4.2
'key' in one_dict.keys()

# 4.4
fibolist[-1]

# 4.5
sum(fibolist)

# 4.6
fibolist.append(fibolist[-1]+fibolist[-2])
fibolist

# 4.7
fibo_copy = fibolist.copy()
fibo_copy.reverse()
print(fibo_copy)
print(fibolist)

# 4.8
fibo_29473 = 29473 in fibolist
fibo_29473

# 4.9
a = set('abracadabra')
b = set('alacazam')
print(a - b)                              # letters in a but not in b
print(a | b)                              # letters in a or b or both
print(a & b)                              # letters in both a and b
print(a ^ b) 

# 4.10
fibo_dict = {}
num = 9
fibo_dict[num] = num in fibolist
fibo_dict