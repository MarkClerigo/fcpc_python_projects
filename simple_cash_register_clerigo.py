list_product=["Piattos", "V-cut", "Chippy", "Mr.Chips", "Tostillas", "RollerCoaster", "ChizCurls", "LaLa", "CloverChips", "Marty's"]
list_price=[13, 14, 7, 8, 8, 6, 6, 7, 8, 7]

for x in range(10):
    print((x + 1), ".", list_product[x], "-", list_price[x])
    
print()
select = input("Select: ")

if select == "1":
    quantity = int(input("Quantity: "))
    total = list_price[0] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "2":
    quantity = int(input("Quantity: "))
    total = list_price[1] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "3":
    quantity = int(input("Quantity: "))
    total = list_price[2] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "4":
    quantity = int(input("Quantity: "))
    total = list_price[3] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "5":
    quantity = int(input("Quantity: "))
    total = list_price[4] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "6":
    quantity = int(input("Quantity: "))
    total = list_price[5] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "7":
    quantity = int(input("Quantity: "))
    total = list_price[6] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "8":
    quantity = int(input("Quantity: "))
    total = list_price[7] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money") 
elif select == "9":
    quantity = int(input("Quantity: "))
    total = list_price[8] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
elif select == "10":
    quantity = int(input("Quantity: "))
    total = list_price[9] * quantity
    print("Total: ", total)
    inputMoney = int(input("Enter money: "))
    if inputMoney >= total:
        print("Change: ", inputMoney - total)
    else:
        print("Not enough money")
else:
    print("Invalid choice")
