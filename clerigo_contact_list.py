print("1 - Add Number")
print("2 - Search Number")

dict_phone = {}
while True:
    choices = (input ("Enter Choices: "))

    if choices == "1":
        name = input("Enter name: ")
        p_num = input("Enter #: ")
        dict_phone[name] = p_num

    elif choices == "2":
        dict_phone[name] = p_num
        Search = input("Enter name: ")
        print(dict_phone[Search])
    else:
        break
