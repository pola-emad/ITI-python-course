
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
def task_3():
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
        
        
        
def task_1():
    tmp_list=[]
    for i in range(5):
        num = int(input('enter a num: '))
        tmp_list.append(num)
    tmp_list.sort()
    sorted_asc = tmp_list.copy()
    tmp_list.sort(reverse=True)
    sorted_desc = tmp_list.copy()
    print(sorted_asc,'\n',sorted_desc)

def task_2():
    big_list  = []
    small_list = []
    num = int(input('enter a num: '))
    for i in range(1,num+1):
        for j in range(1, i+1):
            small_list.append(j*i)
        big_list.append(small_list)
        small_list=[]
    print(big_list)







# task_1()
# task_2()
task_3()
  


