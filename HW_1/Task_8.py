n = int(input('Enter the length of the chocolate bar: '))
m = int(input('Enter the width of the chocolate bar: '))
k = int(input('Enter the number of chocolate pieces: '))
if n <= 0 or m <= 0 or k <= 0:
    print('Entered numbers must be positive')
else:
    if (k % n == 0 or k % m == 0) and k < n * m:
        print(f'Chocolate can be broken into two rectangles')
    else:
        print(f'Chocolate can not be broken into two rectangles')