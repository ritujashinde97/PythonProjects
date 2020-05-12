
def get_price(product,quantity):
    subtotal = price_dict[product] * quantity
    print(product + ':$' + str(price_dict[product]) + '*' + str(quantity) + '=' + str(subtotal))
    return subtotal

def get_discount(bill_price,membership):
    discount = 0
    if bill_price >= 25:
        if membership == 'Gold':
            bill_price = bill_price * 0.75
            discount = 25
        elif membership == 'Silver':
            bill_price = bill_price * 0.85
            discount = 15
        elif membership == 'Bronze':
            bill_price = bill_price * 0.95
            discount = 5
        print(str(discount) + '% off for ' + membership + ' membership at total price no less than $25')
    return bill_price


buying_dict = {'bread': 2, 'butter':3,'milk':4}
price_dict ={'biscuit':1,'butter':2, 'milk':6, 'cornflakes':8, 'maggie': 3, 'bread':2}

bill_price = 0

for key , value in buying_dict.items():
    bill_price += get_price(key,value)

membership = 'Gold'

bill_price = get_discount(bill_price,membership)
print('The total price is $ ' + str(bill_price))
