from random import randrange

def setup():

    amount_of_rolls = 0
    amount_of_dices = 0

    while True:
        try:
            amount_of_dices = int(input("How many dices would you like to roll? "))
            amount_of_rolls = int(input("How many rolls would you like to have for each dice? "))
        except:
            print("ERROR! Please try again and choose a number!")
            continue

        break

    return [amount_of_rolls, amount_of_dices]

def main():
    while True:
        settings = setup()
        stats = {}
        total_sum = 0
        total_product = 0

        for i in range(1, settings[1] + 1):
            stats[f"Dice #{i}"] = [randrange(1, 7) for x in range(1, settings[0] + 1)]

        for k, v in stats.items():
            sum = 0
            for item in v:
                sum += item

            print(f"{k}: {v} - Sum: {sum}")
            total_sum += sum

        print(f"Total sum: {total_sum}")

        while True:
            prompt = input("Would you like to roll the dice again (y/n)? ")
            if prompt.lower() == "y":
                break

            elif prompt.lower() == "n":
                print("Thanks for coming!")
                exit()
            else:
                print("ERROR! Please type in either, 'n' or 'y'.")
                continue

        continue



if __name__ == "__main__":
    main()
