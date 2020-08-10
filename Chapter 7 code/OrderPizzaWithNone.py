def orderPizza(size, style='regular', topping=None):
    # Do some calculations based on the size and style
    # Check if a topping was specified
    PRICE_OF_TOPPING = 1.50  # price for any topping

    if size == 'small':
        price = 10.00
    elif size == 'medium':
        price = 14.00
    else: #large
        price = 18.00

    line = 'You have ordered a ' + size + ' ' + style + ' pizza with'
    if topping is None:  # check if no topping was passed in
        print(line +' no topping')
    else:
        print(line, topping)
        price = price + PRICE_OF_TOPPING

    print('The price is $', price)
    print()
    
#The caller could then order a pizza in any of the following ways:   
orderPizza('large')   # large, defaults to regular, no topping

orderPizza('large', style='regular')  # same as above

orderPizza('large', style='regular', topping = 'mushrooms')  

orderPizza('medium', style='deep dish', topping='mushrooms')

orderPizza('small', topping='mushrooms') # style defaults to regular
