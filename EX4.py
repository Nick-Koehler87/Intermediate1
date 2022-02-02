
print('enter 5 inputs bro')

x = 0
k = 0
while k < 5:
    try:
        y = int(input(f'Enter {k + 1} of 5: '))
        x += y
    except:
        print('Nah dawg an intiger try again')
        k = k - 1
    k += 1
print(x)