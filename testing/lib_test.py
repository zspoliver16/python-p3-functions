#!/usr/bin/env python

from lib.functions import greet_programmer, greet, greet_with_default, \
                        add, halve

import io
import sys


class TestGreetProgrammer:
    '''
    function greet_programmer()
    '''

    def test_greet_programmer(self):
        '''
        prints "Hello, programmer!"
        '''

        captured_out = io.StringIO()
        sys.stdout = captured_out
        greet_programmer()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hello, programmer!\n")
