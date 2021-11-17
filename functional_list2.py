
count = 0
num_list = []
while count < 10:
    num = int(input('Enter an integer number: '))
    num_list.append(num)
    count += 1
  
tot = sum(num_list)
length = len(num_list)

average = tot/length

print(tot)
print(length)
print(average)



    