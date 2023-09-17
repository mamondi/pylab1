number = int(input("Введіть число, кратне 7:"))

if number % 7 == 0:
    print(f"{number} - Number is a multiple of 7")
else:
    print(f"{number} - Number is not multiple of 7")