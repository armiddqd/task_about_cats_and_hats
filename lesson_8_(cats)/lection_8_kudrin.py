# THE ALGO #
# 1. Generate a list with 100 Bool items that are False by default
# 2. Create the round counter = 0
# 3. Start the while loop of 100 rounds
# 4. Start the for loop inside that will replace
# False to True and vice versa for specific elements of a list
# 5. Utilize round counter to identify cats that hats need to be
# replaced on current round
# 6. Add 1 to round counter
# 7. Go to the next round and repeat untill 101 round will be reached
# 8. Close the while loop
# 9. Create an empty list of cats places
# 10. Fill the list of cats places with indexes of True values of loop's
# list by another loop. Add +1 for every index on every round
# 11. Print the list of cats places

# btw the complexity is O(100^2)

cats = [False for i in range(100)]

round_counter = 1

# those vars are useless
# second_round_identifier = [i for i in range(1, 100, 3)]
# third_round_identifier = [i for i in range(2, 100, 3)]

# second_cat_identifier = [i for i in range(1, 100, 2)]
# third_cat_identifier = [i for i in range(2, 100, 3)]

while round_counter <= 100:

    # that code I had before changes
    # for i in range(len(cats)):
    #     if round_counter in second_round_identifier:
    #         if i in second_cat_identifier:
    #             cats[i] = not cats[i]
    #     elif round_counter in third_round_identifier:
    #         if i in third_cat_identifier:
    #             cats[i] = not cats[i]
    #     else:
    #         cats[i] = not cats[i]

    for cat in range(0, len(cats), round_counter):
        cats[cat] = not cats[cat]

    round_counter += 1

cats_places = [i+1 for i in range(len(cats)) if cats[i] is True]

print(cats_places)
