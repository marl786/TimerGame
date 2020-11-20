import time
x=0
z=0

c=time.time()
a=(input("Input the name Ali as fast & as many time as you can: "))
while (a=='ALI' or a== 'Ali' or a=='ali') and (x<10):
    x=x+1
    z=z+1
    b=time.time()
    g=b-c
    print(f'Time taken: {g} seconds')
    print()
    a=(input(f"Input {z}: "))
if x<10:
    print('YOU LOST')   
elif (b-c)>7 :
    e=(b-c)
    f=e-7
    print(f'You ran out of time, Your time was {e} seconds that is {f} seconds more than the allowed time limit.')
else:
    print(f'BINGO YOU WON. THE TIME TAKEN WAS: {b-c} seconds.')
