my_list = []
while True:
    name = input("Enter name: ")
    if name == "End":
        break
    my_list.append(name)
list_len = len(my_list)
if list_len % 2 != 0:
    print(my_list[0:4])
else:
    print(my_list[0:int(list_len / 2)])
