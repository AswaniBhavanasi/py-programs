# how to print maxmimun number in the list without using the max function in for loop
'''lst=[10,0,6,8,20,90]
if not lst:
    print('list is empty')
else:
    max_value = lst[0]  
    for num in lst:
        if num > max_value:
            max_value = num

    print("Maximum:", max_value)'''

# how to print minimum number in the list without using the max function in for loop

'''lst=[10,20,8,7,6,5]
if not lst:
    print('lst is empty')
else:
    min_value=lst[0]
    for num in lst:
        if num < min_value:
            min_value =num
    print('minimum:',min_value)
'''


#Python program to print a ascending order in list  without using the sort() function


'''lst=[76, 23, 45, 12, 54, 9]
print("Original List:", lst)

# sorting list using nested loops
for i in range(0, len(lst)):
	for j in range(i+1, len(lst)):
		if lst[i] >= lst[j]:
			lst[i], lst[j] = lst[j],lst[i]
print("Sorted List", lst)'''

#Python program to print a descending order in list  without using the sort() function
'''
lst=[76, 23, 45, 12, 54, 9]  
print('original list:',lst)

for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i]<= lst[j]:
            lst[i],lst[j]=lst[j] ,lst[i]
print('sorted list',lst)
'''
# how to define a list of integers in input function

'''s = input("Enter a list of integers separated by spaces: ")

# Convert the list of strings into a list of integers
lst1 = []
for i in s.split():
    try:
        num = int(i)
        lst1.append(num)
    except ValueError:
        print(f"Skipping '{item}' as it's not a valid integer.")

print("List of integers:", lst1)
'''

# Generate a random integer between 1 and 100 (inclusive)
'''import random
random_int = random.randint(1, 100)
print("Random Integer:", random_int)'''

#how to print max value in set in forloop
'''my_set = {10, 5, 8, 17, 3, 22}

# Convert the set to a list
my_list = list(my_set)

if len(my_list) > 0:
    max_value = my_list[0]  
    for num in my_list:
        if num > max_value:
            max_value = num

    print("Maximum:", max_value)
else:
    print("The set is empty.")
'''
#how to define a set of integers in input function and find the maximum value
'''s = input("Enter a list of integers separated by spaces: ")

# Convert the list of strings into a list of integers
set1 = set()
for i in s.split():
    try:
        num = int(i)
        set1.add(num)
    except ValueError:
        print(f"Skipping '{item}' as it's not a valid integer.")

print("List of integers:", set1)

lst=list(set1)
if len(lst) > 0:
    
    max_value = lst[0]  
    for num in lst:
        if num > max_value:
            max_value = num

    print("Maximum:", max_value)
else:
    print("The set is empty.")
'''

# Python program to convert decimal into other number systems
'''dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")'''


# write a program to count total number of characters in the string(with space)
'''st='python language'
c=0
for i in st:
        c=c+1
print(c)'''

## write a program to count total number of characters in the string(without space)
'''st='python is a programming language'
c=0
for i in st:
    if i == ' ':  
        continue
    c=c+1
print(c)'''
# write a program to count total number of words in the string
'''st='narayana tech house'
print(len(st.split()))'''

#write a program to find the length of each word in the string
'''st='python is a general purpose language'
s=[]
for i in st.split():
    s.append(len(i))
print(s)'''

# write a program to fetch all vowels from the string
'''st='python language'
l=[]
for i in st:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)'''
# write a program to count total number of vowels
'''st='web developer'
c=0
for i in st:
    if i in 'aeiou':
        c=c+1
print(c)'''

# write a program to count total number of consonants  in the string
'''st='full stack developer'
c=0
for i in st:
    if i not in 'aeiou':
        if i ==' ':
            continue
        c=c+1
print(c)'''

# write a program to fetch all words which starts with vowels from given string
'''st='python is simple and easy language'
s=[]
for i in st.split():
    if i[0] in 'aeiou':
        s.append(i)
print(s)'''

# write a program to fetch the first and last character from each word in the string
'''st='python is high level language'
print([i[0]+i[-1] for i in st.split()])'''

# write a program to fetch all words which contains odd number of character in the string
'''st='python is high level language'
lst=[]
for i in st.split():
    if len(i)%2!=0:
        lst.append(i)
print(lst)'''

# write a program to fetch all words which contains even number of character in the string
'''st='python is high level language'
lst=[]
for i in st.split():
    if len(i)%2==0:
        lst.append(i)
print(lst)'''
#write a program to fetch all words  which starts and ends with vowels in the string
'''st='python is number one language'
s=[]
for i in st.split():
    if i[0] in 'aeiou' and i[-1] in 'aeiou':
        s.append(i)
print(s)'''
# write a program to fetch all palindrome words from list
'''st=['sam','madam','nani','dad','eye','python']
print([i for i in st if i[-1::-1]  in st])'''


# write a program to longest palindrome word
'''st=['sam','madam','nani','dad','eye','python']
a=[]
for i in st:
     if i == i[-1::-1]:
         a.append(i)
print(max(a))

print(max([i for i in st if i[-1::-1] in i]))'''

# write a program to reverse of each word in the string

'''st='python narayana tech house in hyderabad'
a=[]
for i in st.split(','):
    a.append(''.join(reversed(i)))
print(''.join(a))'''

# write a program to reverse internal content of each word in the string
'''st='durga software solutions'
l=[]
for i in st.split():
    l.append(i[::-1])
print(l)'''

#write a  programe to write vowels in uppercase and consonants in lowercase of same string
'''st='python NArayana  tech house HYDERABAD'
a=[]
for i in st:
    if i in 'aeiouAEIOU':
        a.append(i.upper())
    else:
        a.append(i.lower())
print(''.join(a))
'''
# write a programe to seperate vowels and consonants from string
'''st='python NArayana  tech house HYDERABAD'
a=[]
b=[]
for i in st:
    if i in 'aeiouAEIOU':
        a.append(i)
    else:
        b.append(i)
print(''.join(a+b))'''

#python program to find the number of vowels and consonants in a string

'''st='python narayana ' 
a=[]
b=[]
for i in st:
    if i in 'aeiou':
        a.append(i)
    elif i==' ':
        continue
    else:
        b.append(i)
print('vowels are:',len(a))
print('consonants are :',len(b))
'''

#write a program to remove all vowels in a string

'''s='narayana'
vowels=['a','e','i','o','u']
s1=''
for i in range(len(s)):
    if s[i] not in vowels:
        s1=s1+s[i]
print(s1)'''

# write a program to count total number of special characters in the string
'''st='na@#$%&rayana'
import string
lower=string.ascii_lowercase
c=0
for i in st:
    if i not in lower:
        c=c+1
print(c)'''

#write a program to count the occurances of each vowel in the string
'''st='python narayana'
v='aeiou'
d={}.fromkeys(v,0)
for i in st:
    if i in d:
        d[i]=d[i]+1
print(d)'''

#write a program to reverse the dict
'''d={'a':10,'b':20,'c':90}
lst=list(d.items())
lst.reverse()
d1={}
for key,value in lst:
    d1[key] =value
print(d1)
'''
