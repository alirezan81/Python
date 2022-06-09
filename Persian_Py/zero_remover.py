a = [1,0,2,3,0,4,0,5,6]


# create new list
b = [i for i in a if i]
print(b)


c = filter(lambda x: x , a)

print(list(c))


# inplace
for n in a[:]:
    if not n:
        a.remove(n)
print(a)

