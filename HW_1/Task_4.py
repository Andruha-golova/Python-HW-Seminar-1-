S = int(input('Enter the total number of cranes, a multiple of 6: '))

if S % 6 == 0:
    x = S // 6
    print(f'Petya made {x} cranes')
    print(f'Serezha made {x} cranes')
    print(f'Katya made {4 * x} cranes')
else:
    print('The number entered is not a multiple of 6. Please enter another number')