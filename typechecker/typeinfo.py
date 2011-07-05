#-*- coding:utf-8 -*-
'''
This module provides dynamic type check mechanism.

>>> @typeinfo(int, x=int, y=int)
... def add(x, y):
...     return x + y
>>> add(10, 20)
30
>>> add('aa', 'bb')
TypeError

'''

import functools
import inspect
import sys



def _assign_arg(spec, argl, argd):

    placedargs = dict(zip(spec.args, argl))

    left = spec.args[len(placedargs):]

    return dict(placedargs, **dict((a, argd[a]) for a in left if a in argd))



def _get_typeinfo_string(tinfo):

    if isinstance(tinfo, type):
        return tinfo.__name__
    
    if isinstance(tinfo, (tuple, list)):
        return '({0})' % (', '.join(_get_typeinfo_string(x) for x in tinfo))

    return str(tinfo)



def _check_typeinfo(f, spec, types):

    asnames = set(spec.args)
    tnames = set(types.keys())

    for n in asnames - tnames:
        msg = '''In function {0}, argument "{1}" don't have type information.'''
        raise TypeError(msg.format(f.__name__, n))


    for n in tnames - asnames:
        msg = '''In function {0}, typeinfo "{1}({2})" is not used.'''
        raise TypeError(msg.format(f.__name__, n, types[n]))



def _check_arg(f, assigned, tinfo):

    asnames = set(assigned.keys())
    tnames = set(tinfo.keys())


    for n in asnames - tnames:
        msg = '''In function {0}, argument "{1}" don't have type information.'''
        print >> sys.stderr, msg.format(f.__name__, n)


    for n in tnames - asnames:
        msg = '''In function {0}, typeinfo "{1}({2})" is not used.'''
        print >> sys.stderr,  msg.format(f.__name__, n, tinfo[n])

    for n in tnames & asnames:

        arg = assigned[n]
        typ = tinfo[n]

        if not isinstance(arg, typ):
            msg ='In function {3}, argument "{0}" required "{1}". "{2}" found.'
            raise TypeError(msg.format(n,
                                       _get_typeinfo_string(typ),
                                       type(arg).__name__,
                                       f.__name__))



def typeinfo(rettyp, **types):
    '''
    assigning type information to function or method.

    first argument is type information for return value.
    keyword arguments are type informations dictionary for arguments of function.
      eg: arg1=str, arg2=int
    '''

    def decorator(f):

        spec = inspect.getargspec(f)

        defaults = spec.defaults if spec.defaults is not None else ()

        defaultdict = dict(zip(reversed(spec.args),
                               reversed(defaults)))

        _check_typeinfo(f, spec, types)

        @functools.wraps(f)
        def call(*argl, **argd):

            assigned = dict(defaultdict, **_assign_arg(spec, argl, argd))

            _check_arg(f, assigned, types)

            result = f(*argl, **argd)

            if not isinstance(result, rettyp):
                msg = '''return value required "{0}". "{1}" found.'''
                raise TypeError(msg.format(_get_typeinfo_string(rettyp),
                                           type(result).__name__))

            return result

        return call

    return decorator




