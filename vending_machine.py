"""
A virtual vending machine.
"""


class InsufficientFunds(Exception):
    """
    Exception used to indicate that there isn't
    enough money to make a purchase.
    """
    pass

# the allowed coins should be in descending order
ALLOWED_COINS = ( 200, 100, 25, 10, 5 )

# the available products, along with their prices in cents
AVAIL_PRODUCTS = { "drink": 275, "chips": 225, "candy": 315 }

# if the coin is allowed, then append it to the list of inserted coins
def insert_coin( coin, inserted_coins ):
	if ( coin in ALLOWED_COINS ):
		inserted_coins.append( coin )
	else:
		raise ValueError( "invalid coin" )

# if the product is available, then return the amount of change due
def buy_product( product, balance ):
	if ( product not in AVAIL_PRODUCTS ):
		raise ValueError( "product not available" )
	elif ( balance < AVAIL_PRODUCTS[ product ] ):
		raise InsufficientFunds()
	else:
		return ( balance - AVAIL_PRODUCTS[ product ] )

# compose the balance with allowed coins
def return_change( balance ):
	coins = []
	for coinVal in ALLOWED_COINS:
		while ( balance >= coinVal ):
			coins.append( coinVal )
			balance = balance - coinVal
	return coins
