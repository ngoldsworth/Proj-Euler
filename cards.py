import itertools

jack, queen, king = (10, 10, 10)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, king, queen]
working_combos = []

for j in range(len(cards)):
    for combo in itertools.combinations(cards, j):
        if sum(combo) == 21:
            working_combos.append(combo)

print(len(working_combos), working_combos)