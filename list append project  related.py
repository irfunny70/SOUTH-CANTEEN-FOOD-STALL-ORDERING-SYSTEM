order = []
quantity = []


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

    #get input from user
    item = input("what do you want?")
    qty=int(input("how many do you want?"))
    add_on = input('Any add-on?').lower()

    #update our list
    order.append(item,add_on)
    quantity.append(qty)

    #Display current order
    print(f"you have ordered {order},{quantity}")
    conti=input("continue shopping?").lower()
    if conti!="y":
        break




# this is a clue for the project but i javent integrate it yet to top half
print(order, quantity)
# calculation part
price= {'01':5.80, '02':5.90, '03':6.30, '04':6.20}
#this is to show the price of each item
# for i in order:
#     print(i,price[i])

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
        # sum = sum+a[i] same meaning same same
    return sum
print(f'sum of {sum(amount):.2f}')

# need to add modfying fuctiontion like if the person wat to make changes to the order or change the quantity the code need to see what to delete form the list
stu= input("Are you a student(y/n)?").lower()
staff = input("Are you a staff(y/n)?").lower()
