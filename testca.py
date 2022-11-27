# ct = (8,1,5)
# python = ct.update(7,)
# print(python)

#print(list(map((lambda a:a**2), filter((lambda as:a%2==0), range(15)))))

#ct = [x for x in (x for x in 'CT 22966 for CodeTantra' if x.isdigit()) if (x in ([x for x in range(20)])) ]
#print(ct)

# x = ('count',)
# m = 2
# for k in range(int(m)):
#     x=(x,)
#     print(x)

# def func(name,val1):
#     print(name(val1))
# func(max,[1,2,3])
# func(min,[1,2,3])

num = [[[24,6],[8,10]],[[9,18],[12,20]]]
def ct(a):
    b = a[0][0]
    for i in a:
        for j in i:
            if b<j:
                b=j
    return b
print(ct(num[1]))