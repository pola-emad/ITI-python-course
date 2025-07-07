def mario_pyramid(num):

    stars = 1
    spaces = num-1
    for i in range(num):
        print(" "*spaces+"*"*stars)
        stars+=1
        spaces-=1