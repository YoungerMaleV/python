#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

_author_='Younger Man'

import sys

def test():
    args=sys.argv
    if len(args)==1:
        print('Hello China')
    elif len(args)==2:
        print('Hello %s!' % args[1])
    else:
        print('Too many!')

if _name_=='_main_':
    test()
