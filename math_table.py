user_input = int(input('Enter the table you want: '))

for i in range(11):
    if (i == 0):
        continue
    result = (f'{user_input} * {i} = {user_input * i}')
    print(result)
    i+1