
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

for i in num_list:
    if i > average:
        print(i, 'is greater than the average')
    elif i < average:
        print(i, 'is smaller than the average')
    else: 
        print(i, 'is equal to the average')

    