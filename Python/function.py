# def times(x,y):
#    return x*y
#print(times(10, 7))
#print(times(8, 7))


# def faktoriyel(x):
#    fak = 1
#    if(x == 1):
#        return 1
#    else:
#        for item in range(1,x):
#            fak *= item
#    return fak
# print(faktoriyel(6))

# define an "intersect" function that returns the intersection list of two sequences:
# def intersect(seq1, seq2):
#    res = []
#    for x in seq1:
#        if x in seq2:
#            res.append(x)
#    return res
#s1 = "Apple"
#s2 = "Grape"
#print(intersect(s1, s2))
def kwonly(a, *, b, c):  # function does not accept a variable-length argument list
    print(a, b, c)
print(kwonly("abc",b=11,c=788))

