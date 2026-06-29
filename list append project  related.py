order = []
quantity = []
price = {
    # Main Dishes
    '01': 5.50, '02': 5.90, '03': 6.30, '04': 6.20,
    '05': 5.80, '06': 5.90, '07': 6.30, '08': 5.60,
    # Add-ons
    'A1': 0.50, 'A2': 0.80, 'A3': 0.50, 'A4': 3.50, 'A5': 3.50, 'A6': 1.50
}

while True:
    #Show the menu
    main_dish = [
        ('01 - Ayam Bakar Set ', "$5.50"),
        ("02 - Dori Bakar Set", "$5.90"),
        ("03 - Ayam Bakar Set", "$6.30"),
        ("04 - Gulai Ayam Set", "$6.20"),
        ("05 - Ayam penyet Set", "$5.80"),
        ("06 - Dori penyet Set", "$5.90"),
        ("07 - Ayam penyet Set(Boneless)", "$6.30"),
        ("08 - Ayam penyet Set(Wing)", "$5.60"),
    ]

    print(f"===== Penyet + BBQ SET MEAL=====")
    for name, cost in main_dish:
        print(f"{name:<52} {cost:>7}")

    print("\n===== Add On =====")
    items = [
        ("A1 - Rice", "$0.50"),
        ("A2 - Egg", "$0.80"),
        ("A3 - Chili", "$0.50"),
        ("A4 - Fried/Grilled Dori Fish (per piece)", "$3.50"),
        ("A5 - Fried/Grilled chicken leg quarter (per piece)", "$3.50"),
        ("A6 - Fried Chicken Wing (1pc)", "$1.50"),
    ]

    for name, cost in items:
        print(f"{name:<52} {cost:>7}")
    # get input from user
    items=input("\nWhat main dish do you want?")
    if items in price:
        qty=int(input("how many do you want?"))
        order.append(items)
        quantity.append(qty)
        print(f"Added Main Dish {items} x{qty}")
    else:
        print("Invalid")
    #update our list
    add_on=input("Do you want an add-on? (y/n): ").lower()
    if add_on=="y":
        addon_choice=input("Enter add-on").lower()
        if add_on in price:
            addon_qty=int(input("how many add-ons do you want?"))
        order.append(addon_choice)
        quantity.append(addon_qty)
        print(f"Added Add-on {addon_choice.upper()} x{addon_qty}")
    else:
        print("Invalid add-on")
    #Display current order
    print(f"\nCurrent Cart: Items: {order} | Quantities: {quantity}")

    conti=input("Continue shopping? (y/n): ").lower()
    if conti !="y":
        break
print("\n==============================================")
print("                    RECEIPT                   ")
print("==============================================")





# # this is a clue for the project but i havent integrate it yet to top half
# print(order, quantity)
# # calculation part
# price= {'01':5.80, '02':5.90, '03':6.30, '04':6.20}
# #this is to show the price of each item
# # for i in order:
# #     print(i,price[i])

amount = []
for i in range(0,len(quantity)):
    print(f"{order[i]}, {quantity[i]},{price[order[i]]},${quantity[i]*price[order[i]]:.2f}")
    amount.append(round(quantity[i]*price[order[i]],2))
print(amount)
#
#
def sum(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
        # sum = sum+a[i] same meaning same
    return sum
print(f'sum of {sum(amount):.2f}')
