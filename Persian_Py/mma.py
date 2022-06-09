def ma(t):
    d = dict.fromkeys(('max','min','avg'),t[0])
    total = 1
    for n in t[1:]:
        if n > d['max']: d['max'] = n
        if n < d['min']: d['min'] = n
        d['avg'] += n
        total += 1
    d['avg'] /= total
    return d

print(ma([14,10,2,19,15,13,20]))
                
def my_fun(x):
    return {'max':max(x) , 'min': min(x) , 'avg':sum(x) / len(x)}

print(my_fun([14,10,2,19,15,13,20]))
