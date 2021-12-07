import random

##########################################################################

contract_fee = float(input('Enter your monthly contract fee: '))
monthly_calls = float(input('Enter your total call time in minutes: '))
monthly_data = float(input('Enter your total data usage in MB: '))

data_cap = 10000
calls_cap = 500
add_data = 0
add_calls = 0

if monthly_calls > calls_cap:
    add_calls += monthly_calls - calls_cap

if monthly_data > data_cap:
    add_data += monthly_data - data_cap

bill = float(contract_fee + 0.01 * add_data + 0.1 * add_calls)

output = "bill is {0:0.2f} and your name is {1}"

print(output.format(10.5555555, "Quinn"))
print(output.format(20, "Wojtek"))
print(output.format(30.987698769876, "Charlie"))

print('Your bill comes to %.2f' % bill)
########################################################################################################################

num = random.randint(0, 10)

print('Guess a number between 1 and 10')
attempt = 5
msg = 'Too many attempts!'

while attempt > 0:
    user_input = input('Enter Number: ')

    try:
        user_input = int(user_input)
    except:
        print("Only enter numbers")
        continue

    if user_input == num:
        msg = 'You Won!'
        break

    elif user_input > num:
        print(f'{user_input} is greater.\nRemaining attempts: {attempt - 1}.')
        attempt -= 1

    elif user_input < num:
        print(f'{user_input} is smaller.\nRemaining attempts: {attempt - 1}.')
        attempt -= 1

    else:
        print('Something went wrong!')
        break

print(msg)

########################################################################################################################
play = "Y"
while play != "N":
    rnd_num = random.randint(0, 10)
    tries = 0
    guess = -1

    while guess != rnd_num and tries < 5:
        guess = input("Guess a number - attempt " + str(tries))

        try:
            guess = int(guess)
        except:
            print("Only enter numbers")
            continue

        if guess > rnd_num:
            print("Too High")
        elif guess < rnd_num:
            print("Too Low")

        tries += 1

    if guess == rnd_num:
        print("You Win")
    else:
        print("You Lose - number was " + str(rnd_num))

    print("---")
    play = input("Play again? Y/N")
    print("---")

########################################################################################################################

#######################################################################################################################

str_mark_a = input("Enter mark \n")
str_mark_b = input("Enter mark \n")

try:
    int_mark_a = int(str_mark_a)
    int_mark_b = int(str_mark_b)
    final_avg_mark = (int_mark_a + int_mark_b) / 2

    if int_mark_a > 35 & int_mark_b > 35 & int(final_avg_mark) > 40:
        print("Congrats you passed with " + str(final_avg_mark) + " !")
    else:
        print("Oh no you failed =(")

except ValueError:
    print("not a number")


########################################################################################################################
class Chair:
    def __init__(self, seat_type, leg_count):
        self.seat = seat_type
        self.legs = leg_count
        self.price = 100
        self.has_gravity = True
        self.is_sat_on = False

    def print_output(self):
        print("This " + self.seat + " seat has " + str(self.legs) + " and has_gravity is " + str(self.has_gravity))

    def compare_chair(self, other_chair):
        print("Difference in legs is " + str(self.legs - other_chair.legs))

    def while_test(self, time):
        timer = time
        self.is_sat_on = True
        while self.is_sat_on:
            print("I'm being sat on! -> " + str(timer))
            timer -= 1
            if timer <= 0:
                self.is_sat_on = False


stool = Chair("wooden", 3)
throne = Chair("comfy", 4)

stool.print_output()
throne.print_output()

throne.has_gravity = False
throne.print_output()

stool.compare_chair(throne)

throne.while_test(15)

# stool.compare_chair(self=stool, other_chair=throne)

########################################################################################################################
