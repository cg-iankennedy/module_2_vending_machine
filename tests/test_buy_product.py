"""
Tests for the buy_product function
"""
import pytest
from .. import vending_machine

def test_banana():
    with pytest.raises(ValueError):
        change = vending_machine.buy_product( "banana", 300 )

def test_insufficient():
    with pytest.raises(Exception):
        change = vending_machine.buy_product( "drink", 274 )

def test_drink():
    change = vending_machine.buy_product( "drink", 275 )
    assert( change == 0 )

def test_chips():
    change = vending_machine.buy_product( "chips", 225 )
    assert( change == 0 )

def test_candy():
    change = vending_machine.buy_product( "candy", 315 )
    assert( change == 0 )

def test_drink_change():
    change = vending_machine.buy_product( "drink", 300 )
    assert( change == 25 )
