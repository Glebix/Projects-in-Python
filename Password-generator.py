import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
digits_letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


def main():
    password = ''
    while True:
        print("Welcome to Password Generator")
        try:
            length = input("Choose the length  of your password: ")
            length = int(length)
        except:
            length = input("Choose the length of your password: ")
        print("""Choose the difficulty of the password
        1:digits only
        2:letters only
        3:both letters and digits
        4:all values
        
        """)
        try:
            difficulty = int(input('Enter a number from 1 to 4: '))
            if difficulty > 4 or difficulty <= 0:
                difficulty = int(input('Enter a number from 1 to 4: '))
        except:
            difficulty = int(input('Enter a number not a string: '))

        if difficulty == 1:
            for _ in range(length):
                password = password + random.choice(digits)
        elif difficulty == 2:
            for _ in range(length):
                password = password + random.choice(letters)
        elif difficulty == 3:
            for _ in range(digits_letter):
                password = password + random.choice(digits_letter)
        else:
            for _ in range(length):
                password = password + random.choice(printable)
        print(password)
        ans = input("Do you wanna new password: ")
        if ans.lower() == 'y' or ans.lower() == 'yes':
            main()
        else:
            quit()


main()
