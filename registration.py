import string
import pymysql
connection=pymysql.connect(host='localhost',user='root',password='root',db='reglogindb')
c=connection.cursor()

#updating passwords

c.execute('select * from users;')
data=c.fetchall()
print(data)

all_existing_users={}
for i in data:
    all_existing_users[i[2]]=i[3]

print(all_existing_users)

while True:
    login_user =input('enter username:')
    if login_user not in all_existing_users:
        print('invalid user')
        continue
    else:
        while True:
            login_password =input('enter password:')
            if all_existing_users[login_user]!=login_password:
                print('invalid password')
                continue
            else:
                print('login successfull,please password updated')
                print()
                while True:
                    pwd1=input('enter new password:')
                    pwd2 =input('enter confirm password:')

                    if pwd1!= pwd2:
                        print('passwords are mismatch')
                        continue
                    elif len(pwd1) < 8:
                     
                         print('password must have atleast 8 character')
                         continue
                    elif len([i for i in pwd1  if i in string.ascii_lowercase]) ==0:
                
                        print('password must contain atleast one lowerecase character')
                        continue
                    elif len([i for i in pwd1 if i in string.ascii_uppercase])==0:
                        print('passwprd must contain atleast one uppercase')
                        continue
                    elif len([i for i in pwd1 if i in string.digits])==0:
                        print('password must contain atleast one digit')
                        continue
                    elif len([i for i in pwd1 if i in string.punctuation])==0:
                        print('password must contain atleast one special character')
    
                        continue   
                    else:
                        c.execute('update users set password=%s,confirm_password=%s where username=%s',(pwd1,pwd2,login_user))
                        connection.commit()
                        print('passwords are updated')
                        connection.close()
                        break
                break
            break

#login
'''
c.execute('select * from users;')
data=c.fetchall()

all_existing_users={}
for i in data:
    all_existing_users[i[2]] = i[3]

while True:
    login_user=input('enter username:')
    
    if login_user not in all_existing_users :
        print('{} is invalid user,please give correct '.format(login_user))
        continue
    else:
        while True:
            
            login_pwd=input('enter password')
            if all_existing_users[login_user] !=login_pwd:
                print('invalid password,please give correct')
                continue
            else:
                print('login success')
            break
    break
    
'''
#registration
'''while True:
    
    uname=input('enter user name:')
    c.execute('select * from users')
    data=c.fetchall()
    existing_users=[]
    for i in data:
        existing_users.append(i[2])
    if uname in existing_users:
        print('{} is already existed ,please try new username'.format(uname))
        continue
    else:
        while True:
            pwd1=input('enter password:')
            pwd2=input('enter confirm password:')
            if pwd1 !=pwd2:
                print('passwords does not match ,plase give same password')
                continue
            elif len(pwd1)<8:
                print('password must contain atleast 8 characters')
                continue
            elif len([i for i in pwd1  if i in string.ascii_lowercase]) ==0:
                
                print('password must contain atleast one lowerecase character')
                continue
            elif len([i for i in pwd1 if i in string.ascii_uppercase])==0:
                print('passwprd must contain atleast one uppercase')
                continue
            elif len([i for i in pwd1 if i in string.digits])==0:
                print('password must contain atleast one digit')
                continue
            elif len([i for i in pwd1 if i in string.punctuation])==0:
                print('password must contain atleast one special character')
                
            else:
                fname=input('enter first name:')
                lname=input('enter last name:')
                email=input('enter email id:')
                mobile=eval(input('enter mobile number:'))

                c.execute('insert into users values(%s,%s,%s,%s,%s,%s,%s)',(fname,lname,uname,pwd1,pwd1,email,mobile))
                connection.commit()
                print('Registreation is done successfilly')
                connection.close()
            break
    break
  '''

                          


                
            






