#right angle pattern
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end='')
    print()'''
# odd numbers of right angle pattern
'''n=int(input('enter a number of rows:'))
k=1
for i in range(1,n+1):
    for j in range(1,k+1):
        print('*',end='')
    k=k+2
    print()'''

#
'''
n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')

    print()
enter a number of rows:5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * '''
#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()
enter a number of rows:5
* 
* * 
* * * 
* * * * 
* * * * * '''

#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print('*',end=' ')
    print()

enter a number of rows:5
* * * * * 
* * * * 
* * * 
* * 
* 
'''

#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(' ',end=' ')
    for k in range(1,i+1):
        print('*',end=' ')
    print()
enter a number of rows:5
        * 
      * * 
    * * * 
  * * * * 
* * * * *   '''

#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,i):
        print(' ',end=' ')
    for k in range(1,n+2-i):
        print('*',end=' ')
    print(end='\n')
enter a number of rows:5
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
'''

#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=' ')
    print()
enter a number of rows:5
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 '''

#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()
enter a number of rows:5
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
'''
#
'''n=int(input('enter a number of rows:'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=' ')
    print()
enter a number of rows:5
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5''' 
