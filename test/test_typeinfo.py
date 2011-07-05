#-*- coding:utf-8 -*-


from typechecker import typeinfo



def check(func, error, *args, **argd):

    try:
        func(*args, **argd)
    except error, e:
        pass
    else:
        raise
    


def test_check():

    @typeinfo.typeinfo(int, x=int, y=int)
    def add(x, y):

        return x + y


    add(10, 20)


    try:
        add(1.0)
    except TypeError, e:
        pass
    else:
        raise


    @typeinfo.typeinfo(object, x=(int, float))
    def test(x):
        pass

    test(10)
    test(21.0)

    check(test, TypeError, 'aa')



        
