list = []

file = open('passwords.txt')
list = file.read().splitlines()

valid_passwords = 0

for pw in list:
    x_valid = False
    y_valid = False
    x = pw[:pw.index('-')]
    y = pw[pw.index('-')+1:pw.index(' ')]
    let = pw[pw.index(' ')+1:pw.index(':')]
    password = pw[pw.index(':')+2:]

    if password[int(x)-1] == let:
        x_valid = True
    if password[int(y)-1] == let:
        y_valid = True

    if (x_valid == True and y_valid == False) or (x_valid == False and y_valid == True):
        valid_passwords += 1

print(valid_passwords)

