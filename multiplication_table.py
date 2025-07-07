def mult_table_from_1(num):
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(f"{i}x{j} = {j*i}")
def mult_table_from_1_listed():
    big_list  = []
    small_list = []
    num = int(input('enter a num: '))
    for i in range(1,num+1):
        for j in range(1, i+1):
            small_list.append(j*i)
        big_list.append(small_list)
        small_list=[]
    print(big_list)
