#-*- coding:utf-8 -*-
'''
This module provides dynamic type check mechanism.

  >>> from typechecker.typeinfo import typeinfo
  >>> @typeinfo(int, x=int, y=int)
  ... def add(x, y):
  ...     return x + y
  >>> add(10, 20)
  30
  >>> add('aa', 'bb')
  TypeError

'''

__version__ = '0.1.0'
__author__ = 'Shoma Hosaka'
__license__ ='LGPL'

