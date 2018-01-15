favorite_numbers = {
    'aney': [42, 17],
    'Zain': [42, 39, 56],
    'Sherry': [7, 12],
    }

for name, numbers in favorite_numbers.items():
    print("\n" + name.title() + " likes the following numbers:")
    for number in numbers:
        print("  " + str(number))