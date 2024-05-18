my_dict = {"dad": "Eise", "sister_1": "Iris", "sister_2": "Nicky"}
key = input('Enter your key to find it:')

findit= False
for name in my_dict.keys():
    if name == key:
        print(f'{key} is in the dictionary')
        findit =True
        break
if not findit:
    print(f"{key} is not in dictionary.")
    my_dict.update({key:'empty'})
    print(my_dict)
