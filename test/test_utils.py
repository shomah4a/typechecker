#-*- coding:utf-8 -*-


from typechecker import utils


def test_types():


    class cls(object):

        def __call__(self):
            pass


        def __enter__(self):
            pass

        def __exit__(self):
            pass


        def write(self):
            pass


        def read(self):
            pass
        

    def func():
        pass


    assert isinstance(cls, utils.Callable)
    assert isinstance(func, utils.Callable)
    assert isinstance(cls(), utils.Callable)
    assert not isinstance(10, utils.Callable)


    assert isinstance(cls(), utils.ContextManager)
    assert isinstance(cls(), utils.ContextManager)
    assert isinstance(cls(), utils.Writable)



def test_list():

    intlist = utils.list(int)

    assert isinstance([1], intlist)
    assert not isinstance([1.0], intlist)
    assert not isinstance('aa', intlist)



def test_tuple():

    tp = utils.tuple(int, float)

    assert isinstance((1, 0.0), tp)
    assert not isinstance((1, 0), tp)
    assert not isinstance('aa', tp)
