#!/usr/bin/env python

import runpy

class TestAssertionError:
    '''
    an_assertion_error.py
    '''

    def test_assertion_error(self):
        '''
        evaluates two equal values
        '''

        runpy.run_path('lib/an_assertion_error.py')

