my_list=["i", "d", "l", "e"]

print(my_list) #prints['i','d','l','e']

del my_list[2:4]

my_list[1] = "n"

new_list = ["s"] + my_list

new_list.append("g")

print(my_list) # prints ['i','n']
print(new_list) #prints ['s','i','n','g']