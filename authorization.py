def check_email(email):

    email = email.strip()
    if '@' in email and '.'in email:
        email = email.split('@')
        if '.' in email[-1] and not ('' in email ):
            email[-1] = email[-1].strip()
            email[-1] = email[-1].split('.')
            if not('' in email[-1]):
                return True
    print('invalid email')
    return False      
def authorize_user():
    for i in range(5):
        name = input('enter your name : ')
        name=name.strip()
        if name == '' or name.isdigit():
            print('name cannot be empty or digit')
            continue
        email = input('enter your email: ')

        if check_email(email):
            print(name,'\n',email)
            break
def authorization( name_password):

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
def filter_emails(email_list):
    # filter valid emails
    return filter(check_email,email_list)
def check_email_with_exceptions(email):
    try:
        email = email.strip()
        
        email = email.split('@')
        
        email[-1] = email[-1].strip()
        email[-1] = email[-1].split('.')
        if not('' in email[-1]) and not ('' in email ) and len(email[-1]>1):
            return True
        else:
            return False
    except:
        
        return False      
def authorize_user_with_exceptions():
    for i in range(5):
        name = input('enter your name : ')
        name=name.strip()
        if name == '' or name.isdigit():
            print('name cannot be empty or digit')
            continue
        email = input('enter your email: ')

        if check_email_with_exceptions(email):
            print(name,'\n',email)
            break
    else:
        raise('invalid email')

