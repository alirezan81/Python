def cl(lst):
    for item in lst[:]:
        cl(item) if isinstance(item,list) else lst.remove(item) 
            

t = [4,[3],[5,[6,7],8],9]
            
cl(t)

print(t)
