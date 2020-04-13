

def depth(expr,dlabocina):
    m = dlabocina 
    for i in expr:
        if(isinstance(i,(tuple))):
            returned  = depth(i,dlabocina+1)
            m = max(m,returned)
    return m 


        






arr = ('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),
1), ('/', 5, 2)))
arr2 = ('+', ('expt', 'x', 2), ('expt', 'y', 2)) 


print(depth(arr,1))