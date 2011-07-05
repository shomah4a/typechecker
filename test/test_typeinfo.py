#-*- coding:utf-8 -*-


from typechecker import typeinfo



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



        
