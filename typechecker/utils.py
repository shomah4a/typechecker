#-*- coding:utf-8 -*-


class AttrCheck(type):
    '''
    metaclass for attribute check
    '''

    def __instancecheck__(self, instance):

        return all(hasattr(instance, x) for x in self.ATTRIBUTES)


class AndCheck(type):
    '''
    metaclass for and check
    '''

    def __instancecheck__(self, instance):

        return all(isinstance(instance, x) for x in self.CLASSES)



def has_attributes(*attrs):
    '''
    generate check class
    '''

    class Checker(object):

        __metaclass__ = AttrCheck

        ATTRIBUTES = attrs

    Checker.__name__ = 'hasattr[%s]' % (', '.join(attrs))

    return Checker


has_attrs = has_attributes



def and_(*classes):

    class Checker(object):

        __metaclass__ = AndCheck

        CLASSES = classes

    Checker.__name__ = 'And[%s]' % (', '.join([x.__name__ for x in classes]))

    return Checker



def _make_checker(func, name=None):


    class CheckClass(type):
        '''
        metaclass for general type check
        '''

        def __instancecheck__(self, instance):

            return func(self, instance)


    class Checker(object):

        __metaclass__ = CheckClass


    if name is not None:
        Checker.__name__ = name


    return Checker



Callable = has_attributes('__call__')
Callable.__doc__ = '''
Callable class has __call__() method.
'''

ContextManager = has_attributes('__enter__', '__exit__')
ContextManager.__doc__ = '''
Context Manager class has __enter__() and __exit__() methods.
'''

Writable = has_attributes('write')
Writable.__doc__ = '''
Writable class has write() method.
'''

Readable = has_attributes('read')
Writable.__doc__ = '''
Readable class has read() method.
'''


def list(typ):
    u'''
    list type check
    '''

    def list_check(self, obj):

        if not isinstance(obj, __builtins__['list']):
            return False

        return all(isinstance(x, typ) for x in obj)


    return _make_checker(list_check, 'list[%s]' % typ.__name__)



def tuple(*types):
    u'''
    tuple type check
    '''

    def list_check(self, obj):

        if not isinstance(obj, __builtins__['tuple']):
            return False

        if len(obj) != len(types):
            return False

        return all(isinstance(o, t) for o, t in zip(obj, types))

    return _make_checker(list_check, 'tuple[%s]' % (', '.join([x.__name__ for x in types])))

