list = []

file = open('passwords.txt')
list = file.read().splitlines()

valid_passwords = 0

for pw in list:
    x = pw[:pw.index('-')]
    y = pw[pw.index('-')+1:pw.index(' ')]
    let = pw[pw.index(' ')+1:pw.index(':')]
    password = pw[pw.index(':')+2:]
    counter = 0
    for char in password:
        if char == let:
            counter += 1
    if counter >= int(x) and counter <= int(y):
        valid_passwords += 1

print(valid_passwords)
