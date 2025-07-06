
def task_1( name_password):
    # authorization
    name = input('enter ur name: ')
    for i in name_password:
        if i['name'] == name:
            
            password = input('enter ur password: ')
            if i['password'] == password:
                print (" you are authorized")
            else:
                print (" you are not authorized")
            break
    else:
        print('Unknown user name')
def check_email(email):
    email = email.strip()
    if '@' in email and '.'in email:
        email = email.split('@')
        if '.' in email[-1] and not ('' in email ):
            email[-1] = email[-1].strip()
            email[-1] = email[-1].split('.')
            if not('' in email[-1]):
                return True
    
    return False      
def task_4(emails):
    # no of domains
    return list(map(lambda x: x.split('@')[-1],emails))   
def task_3(email_list):
    # filter valid emails
    return filter(check_email,email_list)

    
    



    
#authorization
name_passwords = [{'name': 'pola', 'password':'1234'},
                  {'name': 'youssef', 'password':'hrv'},
                  {'name': 'ziad', 'password':'asdfe'}]
for i in range(3):
    task_1(name_passwords)
print('\n','*'*20)
#--------------------------

# no of domains
emails = ['afsdfa@gmail.com','grev@yahoo.com','br@hotmail.com','@gmail.com','  @  .com', '.com@gmail','sdf@.com']
print(task_4(emails))
print('\n','*'*20)

#--------------------filtered emails
valid_emails = task_3(emails)
print('valid emails are: ',list(valid_emails))


        