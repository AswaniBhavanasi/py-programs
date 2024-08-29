#sum of even numbers from 1 to 100
'''s=0
for i in range(1,101):
    if i%2==0:
        s=s+i
print('sum of  even numbers from 1 to 100:',s)'''

#anagram of string
'''s1=input('enter a first number:')
s2=input('enter a second number:')

if sorted(s1)==sorted(s2):
    print('anagrams')
else:
    print('not anagrams')
'''
#prime numbers
'''for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)'''
#prime numbers from 1 to 50
'''n1=int(input('enter a number:'))
n2=int(input('enter a number:'))
for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)'''
        
#check the prime number
'''n=int(input('enter a number:'))
for i in range(2,n):
        if n%i==0:
            print('not prime number')
            break
else:
    print(' prime ')'''

#perfect number
'''' 6, 28, 496, and 8128 are the perfect numbers
n=int(input('enter a number:'))
s=0
for i in range(1,n):
    if n%i==0:
        s=s+i
if s==n:
    print('perfect number')

else:
    print('not perfect')'''

#armstrong number
'''Armstrong number is a number that is equal to the sum of cubes of its digits.
For example 0, 1, 153, 370, 371 and 407 are the Armstrong numbers.
n=int(input('enter a number:'))
s=0
temp=n
while temp>0:
    digit=temp%10
    s=s+digit**3
    temp//=10
if n==s:
    print('armstrong')
else:
    print('not armstrong')

'''
#fibonnaci series
'''n=int(input('enter a number:'))
n1=0
n2=1
print('fibonnaci series:' ,n1 ,n2,end=" ")
for i in range(2,n):
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3,end=' ')'''

#factorial number with function
'''n=eval(input('enter a number:'))
def factorial(n):
    if n==1:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(n))
'''
#factorial number with for loop
'''
n=int(input('enter a number:'))
fact=1
if n>0:
    for i in range(1,n+1):
        fact=fact*i
print('the factorial number of 6 is :',fact)'''

#palindrome of a number
'''
n=int(input('enter a number:'))
reverse,temp=0,n
while temp!=0:
    reverse =reverse*10+temp%10
    temp//=10
if reverse==n:
    print('number is palindrome')
else:
    print('number is not palindrome')

a=input('enter a number:')
b=a[::-1]
if a==b:
    print('palindrome')
else:
    print('not palindrome')
'''
#table program
'''n=int(input('enter a number:'))
for i in range(1,11,1):
    print(n,'*',i,'=',n*i)
'''
#calendar
'''import calendar as c
print(c.calendar(2023))'''

#python program to swap the variables

'''x=12
y=13
x,y=y,x
print('the value of x is ',x)
print('the value of y is ',y)'''



#present datatime program
'''import datetime as dt
print(dt.datetime.now())'''


#present calendar
'''import calendar as c
print(c.weekday(2023,4,3))
'''

#reverse of character in each word
'''st=input('enter a string:')
print(' '.join([i[-1::-1] for i in st.split()]))'''

#numpy
'''import numpy as np
a1=np.array([[1,2,4],[3,6,7]])
print(a1)'''

#pandas series
'''import pandas as pd
names=['sai','nani','sam']
s=pd.Series(names)
print(s)'''

#pandas dataframe
'''import pandas as pd
data={'names':['sai','sam'],'fee':[200,400]}
df=pd.DataFrame(data)
print(df)'''

# regular expressions
'''import re
mobile=input('enter a mobile number:')
m=re.fullmatch('[6-9][0-9]{9}',mobile)
if m==None:
    print('invalid number')
else:
    print('valid number')'''

#class
'''class student:
    name='sai'
    fee='1000'
    def learning(self):
        print('student always learning')

s=student()
print(s.name)
print(s.fee)
s.learning()
'''
# break ,continue and  pass statement
'''lst=[2,4,5,8,6,7]
for i in lst:
    pass
    if i==4:
        print("this is continue")
        continue
    elif i==6:
        break
    else:
        print(i)'''

#init example
'''class student:
    def __init__(self,name,fee):

        self.name=name
        self.fee=fee
    def test(self):
        print('my name is',self.name,'and fee',self.fee)
s1=student('sam',1000)
s1.test()'''


#palindrome of a string
'''mystr=input('enter a name:')

mystr=mystr.lower()

rev=reversed(mystr)

if list(mystr)==list(rev):
    print('string is palindrome')
else:
    print('string is not palindrome')'''








            
