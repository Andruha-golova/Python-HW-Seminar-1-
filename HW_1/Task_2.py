n = abs(int(input('enter three-digit number: ')))
if (n) < 100 or (n) > 999:
    print('it,s not a three-digit number, please enter again')
else:
    sum = (n % 10 + (n // 10) % 10 + n // 100)
print(sum)