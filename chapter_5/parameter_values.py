def bar(a ,b ,c ,d = None, e = 5 ):
    print (a + b + c)
    print (d)
    print (e)


bar(1, 2, 3)
bar(1, 2, 3, 4)
bar(1, 2, 3, 4, 5)
bar(1, 2, 3, d=4, e=5)
bar()