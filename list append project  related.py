order = []
quantity = []
addon = []

while True:
    #Show the menu
    main_dish = [
        ("01 - Ayam Bakar Set", "$5.50"),
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

    # find the order name with code the user input
    def find_item(code,menu):
        for name, cost in menu:
            if name.startswith(code): # e.g input "07" mathc with the menu "07 - Ayam penyet Set(Boneless)", "$6.30"
                return name, cost
        return None,None #if not foud

    #get input from user
    item_code = input("what do you want?")
    qty=int(input("how many do you want?"))
    add_on_code = input('Any add-on?(enter or leave blank)').upper()

    #look for item details
    dish_name,dish_price = find_item(item_code,main_dish)
    add_on_name,add_on_price = find_item(add_on_code,items) if add_on_code else (None,None)

    #update our list
    order.append(dish_name)
    addon.append(add_on_name)
    quantity.append(qty)

    #Display current order
    print("\n ====== Order ======          ==== Qty ====")
    for i in range(len(order)):
        print(f"{order[i]:<35} {quantity[i]}")

    print('\n====== Add on ======')
    for i in range(len(addon)):
        if addon[i]: #only appear if they pic an addon
            print(f"{addon[i]:<35} x1")
    # i want to add ask user if they want change quantity or remove an item before finalising

    #
    #continue shopping(last part in the code)
    conti=input("continue shopping?").lower()
    if conti!="y":
        break
