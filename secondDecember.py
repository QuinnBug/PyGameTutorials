import math
import sys
import fractions

num_1 = int(input('First numerator: '))
den_1 = int(input('First denominator: '))
num_2 = int(input('Second numerator: '))
den_2 = int(input('Second denominator: '))
f1_decimal = float(num_1 / den_1)
f2_decimal = float(num_2 / den_2)
ans_decimal = f1_decimal * f2_decimal
ans_num = num_1 * num_2
ans_den = den_1 * den_2

output = "{0}/{1}"
output_decimal = 'Your result to three decimal places is {0:0.3f}.'
print(output_decimal.format(ans_decimal))
print('Your result as a fraction is ' + output.format(ans_num, ans_den) + '.')

top = ans_num  # so we can retain ans_num
bottom = ans_den  # so we can retain ans_den
testing = True
hcf = 0

while testing:
    remainder = bottom % top
    if remainder != 0:  # if we have a remainder then we do not yet have a hcf
        bottom = top  # top goes to bottom
        top = remainder  # the remainder goes on top
    else:
        hcf = top
        testing = False  # we have a result and can break the loop

print('\tThe highest common factor is %d.' % hcf)
if ans_num == ans_den:
    print('\t\tYour reduced result is 1.')
else:
    print('\t\t\tYour reduced result is ' + output.format(int(ans_num / hcf), int(ans_den / hcf)) + '.')

####################################################################################

first_numerator = int(input("Enter the first fraction's numerator: "))
first_denomenator = int(input("Enter the first fraction's denomenator: "))
second_numerator = int(input("Enter the second fraction's numerator: "))
second_denomenator = int(input("Enter the second fraction's denomenator: "))

cross_multi = 0
true_denomenator = 0

if first_denomenator == second_denomenator:
    true_numerator = first_numerator + second_numerator
    print("The fraction is", true_numerator, "/", first_denomenator)
else:
    cross_multi = (first_numerator * second_denomenator) + (second_numerator * first_denomenator)
    true_denomenator = first_denomenator * second_denomenator
    print('The fraction is:', cross_multi, "/", true_denomenator)

choice = input("Would you like to simplify the fraction? Type yes/no: ").lower()

if choice == "yes":
    simple_nume = cross_multi
    simple_denom = true_denomenator
    print("Your simplified fraction is:", fractions.Fraction(simple_nume, simple_denom))

else:
    print("Okay, have a good day!")

##############################################################################

# Sequence of Spades, Hearts, Diamonds and Clubs.

cards = ['King', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen']
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
chosen_number = -1
while True:
    while chosen_number > 52 or chosen_number < 1:
        try:
            chosen_number = int(input('Insert number between 1 and 52: '))
        except:
            continue
    suit_i = math.floor(chosen_number / 13)
    if chosen_number % 13 == 0:
        suit_i -= 1
    print('You have chosen ' + suits[suit_i] + " " + cards[chosen_number % 13])
    chosen_number = -1

############################################################################
import math

while True:
    chosen_number = int(input('Insert number between 1 and 52: '))
    if chosen_number > 52 or chosen_number < 1:
        print('Your number is out of the range. Please try again.', end=' ')
        continue

    card_number, suit = math.modf(chosen_number / 13)

    if card_number == 0:
        suit -= 1

    i = card_number * 13
    if i % 1 >= 0.5:
        i = math.ceil(i)
    else:
        i = math.floor(i)

    print('You have chosen ' + suits[int(suit)] + ' ' + cards[i])

#############################################################################

cards = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
chosen_number = -1
while True:
    while not 0 < chosen_number < 53:
        try:
            chosen_number = int(input('Insert number between 1 and 52: '))
        except:
            print("That's not a number between 1 and 52")

    chosen_number -= 1
    card_number, suit = math.modf(chosen_number / 13)

    print('You have chosen ' + suits[math.floor(suit)] + ' ' + cards[round(card_number * 13)])
    chosen_number = -1
