#for i in range(65,91):
#    print(chr(i),end=' ')



from string import ascii_uppercase as letters

start = 0
for i in range(1,6):  
    print(' '*(5-i)+letters[start:start + (i*2-1)])
    start += (i*2-1)


start = 0
for i in range(1,10,2):  
    print(letters[start:start + i].center(9))
    start += i


'''
A B C D E F G H I J
0 1 2 3 4 5 6 7 8 9

0 0-1  A
1 1-4  BCD
4 4-9  EFGHIJ


'''
