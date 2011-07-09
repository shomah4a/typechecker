#-*- coding:utf-8 -*-
'''
This module provides dynamic type check mechanism.

Normal Type Check:

   >>> from typechecker import typeinfo, list_, tuple_, has_attrs
   >>> @typeinfo(int, x=int, y=int)
   ... def add(x, y):
   ...     return x + y
   >>> add(10, 20)
   30
   >>> add('aa', 'bb')
   Traceback (most recent call last):
     File "<console>", line 1, in <module>
     File "typechecker/typeinfo.py", line 113, in call
       _check_arg(f, assigned, types)
     File "typechecker/typeinfo.py", line 84, in _check_arg
       f.__name__))
   TypeError: In function add, argument "y" required "int". "str" found.

Tuple Type Check:

   >>> @typeinfo(int, val=tuple_(int, str))
   ... def test(val):
   ...     return len(val)
   ...
   >>> test((19, 'aaa'))
   2
   >>> test('aaa')
   Traceback (most recent call last):
     File "<console>", line 1, in <module>
     File "typechecker/typeinfo.py", line 113, in call
       _check_arg(f, assigned, types)
     File "typechecker/typeinfo.py", line 84, in _check_arg
       f.__name__))
   TypeError: In function test, argument "val" required "tuple[int, str]". "str" found.

List Type Check:

    >>> @typeinfo(int, val=list_(int))
    ... def test(val):
    ...     return 10
    ...
    >>> test([1,2,3])
    10
    >>> test([1,2,'aaa'])
    Traceback (most recent call last):
      File "typechecker/typeinfo.py", line 113, in call
        _check_arg(f, assigned, types)
      File "typechecker/typeinfo.py", line 84, in _check_arg
        f.__name__))
    TypeError: In function test, argument "val" required "list[int]". "list" found.

Complex Type Check:
 
    >>> @typeinfo(int, val=tuple_(list_(int)))
    ... def test(val):
    ...     return 10
    ...
    >>> test(([1],))
    10
    >>> test((['aa'],))
    Traceback (most recent call last):
      File "/usr/local/python2.7/lib/python2.7/doctest.py", line 1254, in __run
        compileflags, 1) in test.globs
      File "<doctest typechecker[12]>", line 1, in <module>
        test((['aa'],))
      File "typechecker/typeinfo.py", line 113, in call
        _check_arg(f, assigned, types)
      File "typechecker/typeinfo.py", line 84, in _check_arg
        f.__name__))
    TypeError: In function test, argument "val" required "tuple[list[int]]". "tuple" found.


 Structural subtyping:

    >>> @typeinfo(int, f=Callable)
    ... def test(f):
    ...     return 10
    ...
    >>> test(map)
    10
    >>> test(1)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "typechecker/typeinfo.py", line 113, in call
        _check_arg(f, assigned, types)
      File "typechecker/typeinfo.py", line 84, in _check_arg
        f.__name__))
    TypeError: In function test, argument "f" required "hasattr[__call__]". "int" found.


And check:

    >>> @typeinfo(int, f=and_(Callable, ContextManager))
    ... def test(f):
    ...     return 10
    ...
    >>> test(file)
    10
    >>> test(map)
    Traceback (most recent call last):
      File "<console>", line 1, in <module>
      File "typechecker/typeinfo.py", line 113, in call
        _check_arg(f, assigned, types)
      File "typechecker/typeinfo.py", line 84, in _check_arg
        f.__name__))
    TypeError: In function test, argument "f" required "And[hasattr[__call__], hasattr[__enter__, __exit__]]". "builtin_function_or_method" found.
'''

__version__ = '0.1.1'
__author__ = 'Shoma Hosaka'
__license__ ='LGPL'


from typeinfo import typeinfo
from utils import Callable, ContextManager, \
    Writable, Readable, \
    list as list_, tuple as tuple_, \
    has_attrs, and_

