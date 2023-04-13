num = str(input('enter a six digit number: '))
if len(num) == 6:
    num = int(num) 
    sum1 = 0 
    while num // 1000 > 0:
        sum1 = sum1 + num % 10 
        num //= 10
    else:
        sum2 = num % 10 + num // 10 % 10 + num // 100
    if sum1 == sum2:
        print('Congratulations! You have a lucky ticket!')
    else: 
        print('Unfortunately the ticket is not lucky!') 
else:
    print('The number is not six digits. try again!')