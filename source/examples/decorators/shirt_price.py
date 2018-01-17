# a few fake functions to get shirt prices
# all stores stock t-shirts and dress shirts

# create a decorator that allows you to call all of
# the functions with a choice of shirt and pick the 
# store with the lowest price

# see the function at the bottom to see how this will 
# happen

# hint: use the fact that decorators are run at import time
# this decorator does not need to be a closure

comparator = []




@compare_dec
def buy_from_boutique(shirt_type):
    if shirt_type == 't-shirt':
        return 50, 'boutique'
    else:
        return 100, 'boutique'


@compare_dec
def buy_from_department_store(shirt_type):
    if shirt_type == 't-shirt':
        return 20, 'dept'
    else:
        return 50, 'dept'


@compare_dec
def buy_from_box_store(shirt_type):
    if shirt_type == 't-shirt':
        return 10, 'box'
    else:
        return 30, 'box'


@compare_dec
def buy_from_thrift_store(shirt_type):
    print('thrift', shirt_type)
    if shirt_type == 't-shirt':
        return 1, 'thrift'
    else:
        return 3, 'thrift'
    

def compare_prices():
    price_data = []
    for func in comparator:
        price, store = func('t-shirt')
        price_data.append((price, store))
    print(price_data)
    return sorted(price_data)[0]
    
# will need a non-decorated function to compare prices
# this function will take advantage of the fact that 
# all of these functions have the same signature.
# which store gives you the best price, and what is it?

print(compare_prices())
