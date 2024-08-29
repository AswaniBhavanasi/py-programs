# Questions to Practice (Day 1):
'''
#1. Print your name.
print('my name is aswani')
#2. Print the result of adding two numbers.
a=7
b=9
c=a+b
print('a+b =',c)
#3. Print the result of subtracting two numbers.
a=18
b=9
c=a-b
print('a-b =',c)
#4. Print the result of multiplying two numbers.
a=7
b=9
c=a*b
print('a*b =',c)
#5. Print the result of dividing two numbers.
a=7
b=9
c=a/b
print('a/b =',c)'''

# Questions to Practice (Day - 2):

#1. Declare two variables `a` and `b`, assign integer values to them, and print their sum.
''' - **Expected Output:** The sum of `a` and `b`.
a=2
b=8
c=a+b
print('the sum of ','a' ,'and', 'b' , c)'''
    
#2. Create a variable `name` and assign your name to it. Print a greeting message using your name.
'''- **Expected Output:** Greeting message with your name, e.g., "Hello, John!"
name='aswani'
print('good morning',name)'''

#3. Define a variable `pi` and assign the value of π (pi) to it. Print the value of `pi`.
'''- **Expected Output:** The value of π (pi), e.g., 3.14159.
pi=3.14159
print(pi)'''
#4. Define a variable `is_raining` and ask the user to input either "True" or "False" (as a string). Convert the input to a boolean and print its type.
'''    - **Expected Input:** "True" or "False"
    - **Expected Output:** The data type of the converted boolean.
is_raining = input('Enter True or False:')

is_raining_bool = is_raining.lower() == "true"
print("data  type of the converted boolean:", type(is_raining_bool))'''

#5. Create a string variable `sentence` containing any sentence of your choice. Ask the user to input a number, convert it to an integer, and print the sentence repeated that number of times.
'''- **Expected Input:** A number (e.g., "3")
    - **Expected Output:** The sentence repeated the specified number of times.
sentence= input('Enter a number:')

sentence_int = sentence.lower() == "a number"
print("The sentence repeated the specified number of times:", type(sentence_int))'''


#6. Given two variables `x` and `y`, perform the following operations and print the results:
'''- Addition of `x` and `y`.
    - Subtraction of `y` from `x`.
    - Multiplication of `x` and `y`.
    - Division of `x` by `y`.
    - `x` raised to the power of `y`.
    - The remainder when `x` is divided by `y`.
    - The floor division of `x` by `y`.

x=10
y=9
print(x+y)
print(y-x)
print(x*y)
print(x**y)
print(x%y)
print(x/y)
print(x//y)'''
#7. Define a variable `value` and assign any numerical value to it. Ask the user to input a new value.Update the variable `value` with the new input and print the updated value.
'''- **Expected Input:** A numerical value (e.g., "42")
- **Expected Output:** The updated value of the variable.
value=67
value1=int(input('enter a new number:'))
value=value1
print( 'updated value',value)'''


### Questions to practice (Day 3):
'''What are the expected output of the following expressions?
# 1
result = 10 + 3 * 2 - 8 / 4
print(result)
# 2
result = 4 ** 2 + 5 / 2 * 3
print(result)
# 3
result = (8 + 4) * 3 / 2
print(result)
# 4
result = 16 / 4 + 2 ** 3 - 6
print(result)
# 5
result = 10 - 3 * (4 + 2) / 5
print(result)'''



### Questions to Solve (Day - 4):

#1. Concatenate two strings `str1` and `str2`, and print the result.
'''    - **Expected Input:** str1 = "Hello", str2 = "World"
    - **Expected Output:** "HelloWorld"
s1='hello'
s2='world'
s=s1+s2
print(s)'''
#2. Ask the user to enter their name and a greeting. Concatenate the name and greeting to form a personalized message and print it.
'''    - **Expected Input:** name = "John", greeting = "Hi"
    - **Expected Output:** "Hi John"

n=input('enter a name:')
s='hi'+' '+n
print(s)'''
#3. Create a string `word` and repeat it 5 times. Print the result.
'''- **Expected Input:** word = "Python"
    - **Expected Output:** "PythonPythonPythonPythonPython"
w='python'
print(w*5)'''

#4. Ask the user to enter a word and a number. Repeat the word as many times as the given number and print the result.
'''- **Expected Input:** word = "Hello", number = 3
    - **Expected Output:** "HelloHelloHello"
w=input('enter a word:')
n=int(input('enter a number:'))
s=w*n
print(s)'''
#5. Create a string `sentence` and find its length. Print the length of the sentence.
'''    - **Expected Input:** sentence = "This is a sample sentence."
    - **Expected Output:** 27
sentence='the is my code test'
length=len(sentence)
s=length
print(s)'''
#6. Ask the user to input a sentence. Find the length of the sentence, and print the last character of the sentence.
'''- **Expected Output:** Length of the sentence and the last character.
s=input('enter a sentence:')
length=len(s)
s1=s[-1]
print('lenth of the sentence ',length,'and','last character',s1)'''

#7. Create two strings `str1` and `str2`. Find the lengths of both strings and concatenate them. Print the concatenated string.
'''- **Expected Input:** str1 = "Hello", str2 = "World"
- **Expected Output:** "HelloWorld"
s1='hello'
s2='world'
print(len(s1))
print(len(s2))
s=s1+s2
print(s)'''
#8. Ask the user to enter two words, `word1` and `word2`. Concatenate the two words with a space in between and print the result.
'''- **Expected Input:** word1 = "Hello", word2 = "Python"
    - **Expected Output:** "Hello Python"
s1='hello'
s2='world'
s=s1+' '+s2
print(s)'''
#9. Create a string `pattern` containing "*" character and repeat it to form a pattern. The pattern should have 5 rows. Print the resulting pattern.
'''n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()'''

##Questions to practice (Day - 5)****

#Question 1:
'''Convert the integer 42 to a string.
Expected Input:
value = 42
Expected Output:
result = "42"

n=42
print(type(n))
n=str(n)
print(type(n))'''

#Question 2:
'''Convert the string "123" to an integer.
Expected Input:
value = "123"
Expected Output:
result = 123

s='123'
print(type(s))
s=int(s)
print(type(s))'''

#Question 3:
'''Convert the float 3.14 to an integer.
Expected Input:
value = 3.14
Expected Output:
result = 3

f=3.14
print(type(f))
f=int(f)
print(type(f))
print(f)'''

#Question 4:
'''Convert the string "5.5" to a floating-point number.
Expected Input:
value = "5.5"
Expected Output:
result = 5.5

s='5.5'
print(s)
print(type(s))
s=float(s)
print(s)
print(type(s))'''

#Question 5:
'''Convert the integer 100 to a boolean.
Expected Input:
value = 100
Expected Output:
result = True

i=100
i=bool(i)
print(i)'''

#Question 6:
'''Convert the boolean True to an integer.
Expected Input:
value = True
Expected Output:
result = 1

b=True
b=int(b)
print(b)'''

#Question 7:
'''Convert the string `"False"` to a boolean.
Expected Input:
value = “False”
Expected Output:
result = True

s='false'
s=bool(s)
print(s)'''

### Questions to practice (Day 6):

#1. Example: Get the first character of the sentence.
'''Input: "The sun is shining."
Output: "T"
s="The sun is shining"
print(s[0])'''

#2. Example: Get the last character of the sentence.
'''Input: "She sells seashells by the seashore."
Output: "."
s='she sells seashelles by the seashore.'
print(s[-1])'''
#3. Example: Get the character at index 3.
'''Input: "I love Python!"
Output: "o"
s='I love python'
print(s[3])'''
#4. Example: Get the second last character of the sentence.
'''Input: "Life is beautiful."
Output: "l"
s='life is beautiful.'
print(s[-2])'''

#5. Example: Get a substring from index 7 to index 14 (exclusive).
'''Input: "Welcome to Python programming."
Output: " to Pyt"
s='welcome to python programming.'
print(s[7:14])'''
#6. Example: Get a substring from index -9 to -3.
'''Input: "The future is bright."
Output: "s brig"
s='the future is bright.'
print(s[-9:-3])'''
#7. Example: Get the first six characters of the sentence.
'''Input: "Good things take time."
Output: "Good t"
s='good things take time'
print(s[0:6])'''
#8. Example: Reverse the sentence using slicing.
'''Input: "Python is awesome!"
Output: "!emosewa si nohtyP"
s='python is awesome!'
print(s[-1::-1])'''
#9. Example: Get the length of the sentence using indexing.
'''Input: "Coding is fun!"
Output: 14
s='coding is fun!'
print(len(s))'''

'''a = 5
b = 2-7

print(a == b)  
print(a != b)   
print(a > b)   
print(a < b)   
print(a >= b)
print(a <= b)'''

### Questions to practice (Day 7):

#1. Example: Greater than operator (>)
'''Input: 5 > 3
Output: True
print(5>3)'''
#2. Example: Less than operator (<)
'''Input: 10 < 20
Output: True
print(10<20)'''
'''3. Example: Greater than or equal to operator (>=)
Input: 7 >= 7
Output: True
print(7>=7)
4. Example: Less than or equal to operator (<=)
Input: 15 <= 12
Output: False
print(5<=12)
5. Example: Equal to operator (==)
Input: "hello" == "hello"
Output: True
print('hello' == 'hello')
6. Example: Not equal to operator (!=)
Input: 10 != 20
Output: True
print(10 !=20)
7. Example: Comparing integers and floats
Input: 5.0 > 4
Output: True
8. Example: Comparing strings with different cases
Input: "Hello" == "hello"
Output: False
9. Example: Using relational operators with booleans
Input: True == False
Output: False
10. Example: Comparing strings
Input: "apple" < "banana"
Output: True
11. Example: Comparing None with a string
Input: None == "Python"
Output: False
12. Example: Mixing different types in comparisons
Input: 5 > "3"
Output: TypeError
13. Example: Using relational operators with negative numbers
Input: -10 < -5
Output: True
14. Example: Comparing a string with a number
Input: "42" == 42
Output: False
15. Example: Using relational operators with floating-point precision
Input: 0.1 + 0.1 + 0.1 == 0.3
Output: False 
print(0.1 +0.1+0.1 ==0.3)'''

### Questions to practice (Day 8):

'''1. Example: "and" operator with two True conditions
Input: (10 > 5) and ("apple" == "apple")
Output: True


2. Example: "and" operator with one False condition
Input: (3 < 2) and ("banana" == "orange")
Output: False
3. Example: "and" operator with one True and one False condition
Input: (5 >= 3) and (10 != 10)
Output: False
4. Example: "or" operator with two True conditions
Input: ("car" == "car") or (7 < 9)
Output: True
5. Example: "or" operator with one False condition
Input: ("dog" == "cat") or (6 < 10)
Output: True
6. Example: "or" operator with both False conditions
Input: (2 == 3) or (8 > 15)
Output: False
7. Example: "not" operator with True condition
Input: not (4 <= 3)
Output: True
8. Example: "not" operator with False condition
Input: not ("orange" == "orange")
Output: False
9. Example: "not" operator with "and" and "or"
Input: not ((5 > 3) and ("apple" != "banana"))
Output: False
10. Example: "and" and "not" operators combined
Input: (10 > 5) and not (3 < 2)
Output: True
11. Example: "or" and "not" operators combined
Input: ("cat" == "cat") or not (6 > 10)
Output: True
12. Example: Using parentheses for grouping expressions
Input: ((5 >= 3) and (10 != 10)) or (8 > 15)
Output: False
13. Example: Combining multiple "and" operators
Input: (2 < 5) and (10 == 10) and ("hello" != "world")
Output: True
14. Example: Combining multiple "or" operators
Input: (7 < 3) or (5 >= 5) or ("apple" == "apple")
Output: True
15. Example: Using "not" operator with an expression
Input: not (10 > 5 and "car" != "car")
Output: False
16. Example: Using "not" operator with "or" and "and"
Input: not (5 > 3 or "dog" == "cat" and 7 < 5)
Output: False
17. Example: Combining "and" and "or" operators
Input: (5 > 3 and "apple" != "banana") or (8 == 8 or 6 < 10)
Output: True
18. Example: Combining "or" and "not" operators
Input: ("apple" == "banana" or not (6 > 10))
Output: True
19. Example: Complex combination of "and", "or", and "not"
Input: not (2 < 5 and (7 > 3 or "hello" == "world"))
Output: False
20. Example: Nested use of "and", "or", and "not" operators
Input: (not (5 > 3) and (10 != 10 or "car" == "car"))
Output: False '''


### Questions to practice (Day 9):

#Question 1:**
#Write a program that takes a number as input and prints "Even" if it's an even number, and "Odd" if it's an odd number.
'''n=eval(input('enter a number:'))
if n%2==0:
    print(n,'even number')
else:
    print(n,'odd number')'''
#Question 2:
#Write a program that takes two numbers as input and prints the larger number.
'''s1=eval(input('enter a  first number:'))
s2=eval(input('enter a second number:'))
if s1 >s2:
    print(s1,'first number')
else:
    print(s2,'second number')'''

#Question 3:
#Write a program that takes a character as input and prints "Vowel" if it's a vowel (a, e, i, o, u), and "Consonant" otherwise.
'''n=input('enter a character:')
vowel='aeiou'
if n in vowel:
    print('vowels')
else:
    print('consonant')'''

#Question 4:
#Write a program that takes a year as input and prints "Leap Year" if it's a leap year, and "Not a Leap Year" otherwise.
'''n=int(input('enter a year:'))
if n%4==0:
    print(n,'is leap year')
else:
    print(n,'is not a leap year')'''
    
#Question 5:
#Write a program that takes a grade as input (A, B, C, D, or F) and prints "Pass" if it's A, B, C, or D, and "Fail" if it's F.
'''n= input("Enter your grade (A, B, C, D, or F): ")
if n  in ['A','B','C','D','E','F']:
    print('pass')
elif n=='F':
    print('fail')
else:
    print('invalid')'''


### Questions to practice (Day - 10)

#Question 1:
#Check if a given number `num` is positive, negative, or zero.
'''n=int(input('enter a number:'))
if n>0:
    print('positive')
elif n <0:
    print('negative')
else:
    print('zero')'''
#Question 2:
#Determine the type of a given number num: even or odd, and whether it is positive or negative.
'''x =9

if x %2 != 0:
    print("x is odd.")
    if x <0:
        print("x is positive.")
    elif x >0:
        print("x is negative.")
    else:
        print('invalid')
else:
    print("x is even.")'''

#Question 3:
#Classify a given age into four categories: baby, child, teenager, or adult.
'''age=int(input('enter a number:'))
if age==5:
    print('baby')
elif age==10:
    print('child')
elif age==16:
    print('teenager')
else:
    print('adult')'''
#Question 4:
#Assign a grade to a given percentage, considering the following grade scale: A (90-100), B (80-89), C (70-79), D (60-69), and F (below 60).    
'''percentage=int(input('enter a number:'))

if percentage >=90:
    print('grade A')
elif percentage >=80 :
    print('grade b')
elif percentage >=70:
    print('grade c')
elif percentage >=60:
    print('grade d')
else:
    print(' grade f')'''
#Question 5:
#Check if a given year is a leap year, and if it is, find the number of days in February for that year.

'''year = int(input("Enter a year: "))
    
if year < 0:
    print("Invalid year entered.")
else:
    is_leap = False
        
    if year % 4 == 0 :
            is_leap = True
        
    if is_leap:
        print(f"{year} is a leap year.")
        print(f"The number of days in February for {year} is: 29")
    else:
        print(f"{year} is not a leap year.")
        print(f"The number of days in February for {year} is: 28")'''

### Questions to practice (Day - 11)

#Question 1:
#Write a while loop that prints numbers from 1 to 10.
'''i=1
while  i <=10:
    print(i)
    i=i+1'''
#Question 2:
#Create a while loop that calculates the sum of numbers from 1 to n, where n is the input.
'''n=int(input('enter a number:'))
total=0 
i=0
while i<=n:
    total +=i
    i=i+1
print('the sum of numbers from 1 to n is ',total)'''

#Question 3:
#Write a while loop that prints even numbers from 2 to 10.
'''i=2
while i <=10:
    print(i)
    i=i+2'''

#Create a while loop that keeps prompting the user for a number until they enter a negative number.
'''Expected Input: 5, 10, -2
Expected Output: (No output, just prompt for input)
    
while True:
    num = int(input("Enter a number: "))
        
    if num < 0:
        break '''
#Question 5:
#Write a while loop that counts down from 10 to 1.
'''i=10
while i>=1:
    print(i)
    i=i-1'''
#Question 6:
#Create a while loop that asks the user to guess a secret number (e.g., 7) and continues until the correct number is guessed.
'''secret_number = 7  # Change this to the desired secret number
guessed = False
    
while not guessed:
    
    guess = int(input("Guess the secret number: "))
        
    if guess == secret_number:
        
        guessed = True
        print("Congratulations! You guessed the correct number.")
    else:
        print("Wrong guess. Try again!")'''


#Question 7:
#Write a while loop that calculates the factorial of a given number.
'''num= int(input("enter a number: "))
 
fac = 1
i = 1
 
while i <= num:
    fac = fac * i
    i = i + 1
 
print("factorial of ", num, " is ", fac)'''

#Question 8:
#Create a while loop that prints the Fibonacci series up to n.
'''n = int(input("Enter the value of n: "))
a, b = 0, 1

print("Fibonacci series up to", n, "is:")
while a <= n:
    print(a, end="\n")
    a, b = b, a + b
'''
#Question 9:
#Write a while loop that reads numbers from the user until they enter the number 0. Then, it prints the sum of all the entered numbers.
'''s = 0

while True:
    num = eval(input("Enter a number: "))
    
    if num == 0:
        break
    
    s+= num

print("Sum of entered numbers:", s)'''


#Question 10:
#Create a while loop that prints the square of numbers from 1 to 5.
'''num = 1

while num <= 5:
    square = num ** 2
    print(square)
    num += 1'''

### Questions to practice (Day - 12):

#1. Write a for loop that prints all numbers from 1 to 5.
'''for i in range(1,6):
    print(i)'''
#2.Use a for loop to calculate the sum of numbers from 1 to 10.
'''s=0
for i in range(1,11):
    s=s+i
print(s)
'''
