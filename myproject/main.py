import random
import data_processing
from verify_guesses import verify_guesses

# Create a function to create a bar plot

# import_file.import_file()
first_position_qty = data_processing.first_position_qty
second_position_qty = data_processing.second_position_qty
third_position_qty = data_processing.third_position_qty
fourth_position_qty = data_processing.fourth_position_qty
fifth_position_qty = data_processing.fifth_position_qty
sixth_position_qty = data_processing.sixth_position_qty


def create_arrays(position_qty):
    x_array = []
    for item in position_qty:
        x_array.append(item[0])

    y_array = []
    for item in position_qty:
        y_array.append(item[1])

    return x_array, y_array


first_x, first_y = create_arrays(first_position_qty)
second_x, second_y = create_arrays(second_position_qty)
third_x, third_y = create_arrays(third_position_qty)
fourth_x, fourth_y = create_arrays(fourth_position_qty)
fifth_x, fifth_y = create_arrays(fifth_position_qty)
sixth_x, sixth_y = create_arrays(sixth_position_qty)

first_x.sort()
second_x.sort()
third_x.sort()
fourth_x.sort()
fifth_x.sort()
sixth_x.sort()


def create_random_play(upper_limit):
    numbers = set()
    while len(numbers) < 6:
        first_guess = random.randint(first_x[0], first_x[upper_limit])
        if first_guess not in numbers:
            numbers.add(first_guess)
        second_guess = random.randint(second_x[0], second_x[upper_limit])
        if second_guess not in numbers:
            numbers.add(second_guess)
        third_guess = random.randint(third_x[0], third_x[upper_limit])
        if third_guess not in numbers:
            numbers.add(third_guess)
        fourth_guess = random.randint(fourth_x[0], fourth_x[upper_limit])
        if fourth_guess not in numbers:
            numbers.add(fourth_guess)
        fifth_guess = random.randint(fifth_x[0], fifth_x[upper_limit])
        if fifth_guess not in numbers:
            numbers.add(fifth_guess)
        sixth_guess = random.randint(sixth_x[0], sixth_x[upper_limit])
        if sixth_guess not in numbers:
            numbers.add(sixth_guess)
    return [first_guess, second_guess, third_guess, fourth_guess, fifth_guess, sixth_guess]
