# THE ALGO #
# 1. Generate a list with 100 Bool items that are False by default
# 2. Create the round counter = 0
# 3. Set 2 lists with generated ranges
# of every second and every third round number
# 4. Set 2 lists with generated ranges of second and third cats
# 4. Start the while loop of 100 rounds
# 5. Start the for loop inside that will replace
# False to True and vice versa for specific elements of a list
# 6. Identify what type of round is it -
# first, second or third by check if counter is in round lists
# 7. Replace the value for every element in a list based on type of round
# 8. Close the while loop
# 9. Create an empty list of cats places
# 10. Fill the list of cats places with indexes of True values of loop's
# list by another loop. Add +1 for every index on every round
# 11. Print the list of cats places

# btw the complexity is O(100^2)

cats = [False for i in range(100)]

round_counter = 0

second_round_identifier = [i for i in range(1, 100, 3)]
third_round_identifier = [i for i in range(2, 100, 3)]

second_cat_identifier = [i for i in range(1, 100, 2)]
third_cat_identifier = [i for i in range(2, 100, 3)]

while round_counter < 100:

    for i in range(len(cats)):
        if round_counter in second_round_identifier:
            if i in second_cat_identifier:
                cats[i] = not cats[i]
        elif round_counter in third_round_identifier:
            if i in third_cat_identifier:
                cats[i] = not cats[i]
        else:
            cats[i] = not cats[i]

    round_counter += 1

cats_places = [i+1 for i in range(len(cats)) if cats[i] is True]

print(cats_places)
