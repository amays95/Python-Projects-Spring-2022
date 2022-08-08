Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
"""
Program Author: Austin Mays
Program Name: coupon_calculations.py
Function: To calculate total cost of a purchase after discounts, tax, and shipping are applied.
Date: 2/27/2022
"""
'\nProgram Author: Austin Mays\nProgram Name: coupon_calculations.py\nFunction: To calculate total cost of a purchase after discounts, tax, and shipping are applied.\nDate: 2/27/2022\n'

price = 20.99
cash_off = 10.00
percent_off = 0.20
tax = 0.06
shipping = 5.95

cash_off_subtotal = price-cash_off
percent_off_subtotal = cash_off_subtotal-percent_off
percent_off_subtotal = percent_off*cash_off_subtotal
subtotal = percent_off_subtotal + cash_off_subtotal
tax total = tax*subtotal
SyntaxError: invalid syntax
tax_total = tax*subtotal
total = tax_total+subtotal+shipping
total
19.92928
20.99-10.00
10.989999999999998
0.20*10.99
2.198
10.99-2.20
8.79
0.06*8.79
0.5274
0.53 + 8.79
9.319999999999999
9.32+5.95
15.27
total = 15.27

if price == 20.99:
    if cash_off == 10.00:
        if percent_off == 0.20:
            if tax == 0.06:
                if shipping == 5.95:
                    print('Your total is $15.27.')
else:
    print('Sales Error')

    
Your total is $15.27.

import ringup
Purchase Amount: 20.99
Cash Coupon Amount: 10.00
Percentage Coupon Amount: 0.20
Tax:0.06
Shipping:5.95
Total = 15.27
Total
15.27
