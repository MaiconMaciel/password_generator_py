import random


def passWord():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
               'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
               'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    if nr_symbols + nr_numbers > nr_letters:
        print(f'The amount of letters and/or Symbols is higher than '
              f'the total of letters. Try again.')
        passWord()
    else:
        nr_letters = nr_letters - (nr_symbols + nr_numbers)
        pass_letters = []
        pass_numbers = []
        pass_symbols = []

        x, y, z = 0, 0, 0
        while x < nr_letters:
            a = random.randint(0, int(len(letters) - 1))
            pass_letters.append(letters[a])
            x += 1

        while y < nr_symbols:
            b = random.randint(0, int(len(symbols) - 1))
            pass_symbols.append(symbols[b])
            y += 1

        while z < nr_numbers:
            c = random.randint(0, int(len(numbers) - 1))
            pass_numbers.append(numbers[c])
            z += 1

        password = pass_numbers + pass_letters + pass_symbols
        random.shuffle(password)
        n_pass = ''
        for i in password:
            n_pass += i

    print(f'Your random password is: {n_pass}')


passWord()