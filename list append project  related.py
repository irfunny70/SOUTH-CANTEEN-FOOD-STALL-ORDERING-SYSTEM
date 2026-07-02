order = []
quantity = []
addon = []
price = {
    # Main Dishes
    '01': 5.50, '02': 5.90, '03': 6.30, '04': 6.20,
    '05': 5.80, '06': 5.90, '07': 6.30, '08': 5.60,
    # Add-ons
    'a1': 0.50, 'a2': 0.80, 'a3': 0.50, 'a4': 3.50, 'a5': 3.50, 'a6': 1.50}
while True:
    #Show the menu

    main_dish = [
        ("01 - Ayam Bakar Set(grilled chicken set)", "$5.50"),
        ("02 - Dori Bakar Set(grilled Dori set)", "$5.90"),
        ("03 - Ayam Bakar Set(grilled boneless chicken set)", "$6.30"),
        ("04 - Gulai Ayam Set", "$6.20"),
        ("05 - Ayam penyet Set(Fried chicken set)", "$5.80"),
        ("06 - Dori penyet Set(Fried Dori set)", "$5.90"),
        ("07 - Ayam penyet Set(Fried Boneless chicken set)", "$6.30"),
        ("08 - Ayam penyet Set(Fried chicken Wing set)", "$5.60"),
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

    # find the order name with code the user input
    def find_item(code,menu):
        for name, cost in menu:
            if name.startswith(code): # e.g input "07" mathc with the menu "07 - Ayam penyet Set(Boneless)", "$6.30"
                return name, cost
        return None,None #if not foud

    #get input from user for dishes and ask till get correct code
    while True:
        item_code = input("\nwhat do you want?")#error check
        # look for item details
        dish_name, dish_price = find_item(item_code, main_dish)
        if dish_name:
            break
        print('Please choose correct option')
    #input qty
    qty = int(input("how many do you want?"))

    #addon is optional but input must be valid if they wnat something
    while True:
        addon_code = input("Any add-on?(add code or leave blank)").upper()
        if addon_code =="":
            add_on_name, add_on_price = None,None
            break
        add_on_name, add_on_price = find_item(addon_code, items)
        if add_on_name:
            break
        print("Please choose correct option")

    #update our list
    order.append(dish_name)
    addon.append(add_on_name)
    quantity.append(qty)

    #Display current order
    print("\n ====== Order ======                           ==== Qty ====")
    for i in range(len(order)):
        print(f"{order[i]:<52} x{quantity[i]}")

    print('\n====== Add on ======')
    for i in range(len(addon)):
        if addon[i]: #only appear if they pic an addon
            print(f"{addon[i]:<52} x1")

    # i want to add ask user if they want change quantity or remove an item before finalising
    change = input('\n Wanna make any changes?').upper()
    if change == 'Y':
        # show order with index numbers so they can pick one
        print("\n your current order")
        for i in range(len(order)):
            print(f"{i + 1}. {order[i]} x{quantity[i]} \n   {addon[i] if addon[i] else ''} ")

        pick = int(input("Which item number do you want to change? ")) - 1

        action = input("choose the following option \n'q' to change quantity: \n'a' to change add-on: \n'ra' to remove dish: \n'rd' to remove add on: ").lower()

        if action == 'ra':
            order.pop(pick)
            quantity.pop(pick)
            addon.pop(pick)
            print("Item removed.")
        elif action == 'rd':
            addon.pop(pick)
            print("Add-on removed")
        elif action == 'q':
            new_qty = int(input("New quantity? "))
            quantity[pick] = new_qty
            print("Quantity updated.")
        elif action == 'a':
            new_addon_code = (input("New add-on? ")).upper()
            if new_addon_code:
                new_addon_name, _ = find_item(new_addon_code, items)
                addon[pick] = new_addon_name
            else:
                addon[pick] = None
            print("Add-on updated.")

    #discount logic
    discount_percentage = 0.0
    stu = input("\nAre you a student (y/n)? ").lower()
    staff = input("Are you a staff (y/n)? ").lower()
    if stu == 'y':
    discount_percentage = 0.10  # 10% Student Discount
    print("Student Discount Applied (10%)")
elif staff == 'y':
    discount_percentage = 0.15  # 15% Staff Discount
    print("Staff Discount Applied (15%)")
discount_amount = subtotal * discount_percentage
grand_total = subtotal - discount_amount
print("\n==============================================")
print("               FINAL RECEIPT                  ")
print("==============================================")

subtotal = 0.0
for i in range(len(order)):
    item_code = order[i]
    item_qty = quantity[i]
    item_unit_price = price[item_code]
    line_total = item_qty * item_unit_price
    subtotal += line_total

    display_code = item_code.upper()
    print(f"Item [{display_code}]  x{item_qty:<3} @ ${item_u
print("----------------------------------------------")
print(f"Total Discount:                      -${discount_amount:.2f}")
print(f"GRAND TOTAL DUE:                      ${grand_total:.2f}")
print("==============================================")

#continue shopping(last part in the code)
conti=input("continue shopping? (y/n)").lower()
if conti != "y":
    break
