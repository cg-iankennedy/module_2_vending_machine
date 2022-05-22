"""
Tests for the return_change function
"""

import pytest
from .. import vending_machine

def test_negative():
    coins = vending_machine.return_change( -10 )
    assert( coins == [] )

def test_zero():
    coins = vending_machine.return_change( 0 )
    assert( coins == [] )

def test_round():
    coins = vending_machine.return_change( 7 )
    assert( coins == [5] )

def test_twentyfive():
    coins = vending_machine.return_change( 25 )
    assert( coins == [25] )

def test_four_dollars():
    coins = vending_machine.return_change( 400 )
    assert( coins == [200,200] )

def test_three_dollars():
    coins = vending_machine.return_change( 300 )
    assert( coins == [200,100] )

def test_many():
    coins = vending_machine.return_change( 265 )
    assert( coins == [200,25,25,10,5] )
