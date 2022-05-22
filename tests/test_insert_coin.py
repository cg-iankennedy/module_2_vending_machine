"""
Tests for the insert_coin function
"""

import pytest
from .. import vending_machine

def test_fifty_cents():
    with pytest.raises(ValueError):
        inserted_coins = []
        vending_machine.insert_coin(50, inserted_coins)

def test_five_cents():
    inserted_coins = []
    vending_machine.insert_coin(5, inserted_coins)
    assert( inserted_coins == [5] )

def test_ten_cents():
    inserted_coins = []
    vending_machine.insert_coin(10, inserted_coins)
    assert( inserted_coins == [10] )

def test_twentyfive_cents():
    inserted_coins = []
    vending_machine.insert_coin(25, inserted_coins)
    assert( inserted_coins == [25] )

def test_loonie():
    inserted_coins = []
    vending_machine.insert_coin(100, inserted_coins)
    assert( inserted_coins == [100] )

def test_toonie():
    inserted_coins = []
    vending_machine.insert_coin(200, inserted_coins)
    assert( inserted_coins == [200] )
