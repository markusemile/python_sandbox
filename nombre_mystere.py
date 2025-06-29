from random import randrange

number = randrange(1, 20)
turn = 1
query_number = ''

while True:
    while not query_number.isdigit():
        query_number = input("Guess the number ! Please enter a number : ")

    query_number = int(query_number)

    if query_number != number:

        if query_number < number:
            print("The number to find is BIGGER")
        else:
            print("The number to find is SMALLER")

        print("Try again !")
        turn += 1
        query_number = ''
    else:
        print(f"Bravo ! You find the right number {number} in {turn} tries !")
        break





