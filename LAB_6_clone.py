# Brian Tang
def encoder(text):
    l = []
    for num in text:
        if num.isdigit():
            num = int(num) + 3
            if num > 9:
                num = num-9
            num = str(num)
        l.append(num)
    return ''.join(l)

def decoder(text):
    l = []
    for num in text:
        if num.isdigit():
            num = int(num) - 3
            if num == 0:
                num = num+6
            num = str(num)
        l.append(num)
    return ''.join(l)

orig = 0
after = 0
print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')
hurr = 0
while hurr == 0:
    op_1 = int(input('Please enter an option: '))
    if op_1 == 1:
        op_2 = input("Please enter your password to encode: ")
        orig = encoder(op_2)
        print('Your password has been encoded and stored!')
    if op_1 == 2:
        after = decoder(orig)
        print(f'The encoded password is {orig}, and the original password is {after}.')
    elif op_1 == 3:
        hurr = 1
        break
