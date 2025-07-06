def task_2(str):
    vowels = "aeiou"
    count = 0
    for i in str:
        if i.lower() in vowels:
            count += 1
    print(f"Number of vowels in {str} is {count}")
def task_3(str):
    print(f"for the string '{str}'")
    for i in range(len(str)):
        if str[i] =="i":
            print(f"Found i at index {i}")
def task_4(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(f"{i}x{j} = {j*i}")
            

def task_5(num):

    stars = 1
    spaces = num-1
    for i in range(num):
        print(" "*spaces+"*"*stars)
        stars+=1
        spaces-=1
task_2('abhkihgO')
print('-'*20)
task_3('bouihihgki')
print('-'*20)
task_4(4)
print('-'*20)
task_5(4)
