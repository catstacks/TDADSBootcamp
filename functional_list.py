my_list=["i", "d", "l", "e"]

print(my_list) #prints['i','d','l','e']

del my_list[2:4] # deletes 'l' and 'e' from list leaving just ['i', 'd']

print(my_list)

my_list[1] = "n" # replaces 'd' with 'n' to give ['i', 'n']

new_list = ["s"] + my_list # adds 's' to start of a new list called new_list ['s', 'i', 'n']

print(new_list)

new_list.append("g") # adds 'g' to end of new_list to give ['s', 'i', 'n', 'g']

print(my_list) # prints ['i','n']
print(new_list) #prints ['s','i','n','g']


new_list.insert(1,"t")
print(new_list) # prints ['s', 't', 'i', 'n', 'g']

import random
letter = random.choice(new_list)
print(letter) # prints any random letter from the list

print(new_list) # prints ['s', 't', 'i', 'n', 'g']

final_list = []
for i in new_list:
  final_list.append(new_list.index(i))
sum(final_list)
len(final_list)

print(final_list) # prints the indexes of the items in the list as a new list [0, 1, 2, 3, 4]