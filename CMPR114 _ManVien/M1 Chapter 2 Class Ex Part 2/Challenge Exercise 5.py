number_shares = 2000
amount_share_purchased = 40
amount_share_sold = 42.75

amount_paid_stock = number_shares * amount_share_purchased
amount_commission1 = amount_paid_stock * 0.03

amount_sold_stock = number_shares * amount_share_sold
amount_commission2 = amount_sold_stock * 0.03

amount_left = - amount_paid_stock + amount_sold_stock - amount_commission1 - amount_commission2

print('The amount of money Joe paid for the stock is $', amount_paid_stock)
print('The amount of commission Joe paid his broker' 
' when he bought the stock is $', amount_commission1)
print('The amount for which Joe sold the stock is $', amount_sold_stock)
print('The amount of commission Joe paid his broker'
' when he sold the stock is $', amount_commission2)
print('The amount of money that Joe had left'
' when he sold the stock and paid his broker (both times) is $', amount_left)

if amount_left > 0:
    print('Joe made a profit.')
else:
    print('Joe lost money.')

