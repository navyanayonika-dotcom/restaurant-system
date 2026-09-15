#restaurant system
customer_name=input('Please enter your name: ').title()
menu={
    'Burger':80,
    'Pizza':100,
    'Biryani':150,
    'Momo':60,
    'Coffee':50,
    'Coke':40,
    'Noodles':70
}
def display_menu(menu):
    print('\n ===========MYSTIC RESTAURANT===========')
    print('-----------------MENU-------------------')

    for item,price in menu.items():
        print(f'{item:<20}Rs.{price}')
    print('----------------------------------------')
print("Welcome to MYSTIC RESTAURANT!Here's our menu: ")
display_menu(menu)
order_total=0
items=0
from datetime import datetime
now=datetime.now()
date=now.strftime('%d:%m:%Y')
time=now.strftime('%I:%M %p')
order=[]
while True:
    item=input('Please enter the item you want to order: ').title()
    if item in menu:
        quantity=int(input('Quantity: '))
        order_total += menu[item]*quantity
        items+=quantity
        order.append((item, quantity, menu[item] * quantity))

    else:
        print('Sorry,the item is not available in our menu.')
    choice=input("Do you want to order anything else?If yes,please enter 'yes'.If you do not wish to order anything else,please enter 'done'." )
    if choice=='yes':
        continue
    elif choice=='done':
        print('Alright,your order is completed.') 
        break
    else:
        print(f'Sorry,{item} is not available in our menu.')



subtotal=order_total
gst_calc=subtotal*0.05
total=subtotal+gst_calc
    


print(f'''
============================
     MYSTIC RESTAURANT
============================
----------------------------
Customer Name:{customer_name}
Date:{date}
Time:{time}
----------------------------
Item     Quantity     Price
----------------------------
''')
for item,quantity,price in order:
            print(f"{item:<15}{quantity:<10}{price}")
print(f''' 
Items Ordered:{items}
-----------------------------
Subtotal:{order_total:.2f}
GST(5%):{gst_calc:.2f}
-----------------------------
Grand Total:{total}
=============================
Payment Status:Paid
Hope you enjoyed your meal.
Thank You!Visit again☺️
''')

