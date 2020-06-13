def pythagorean_trips_from_perimeter(perimeter: int):
    pyth_trips = []
    for c in range(1, perimeter):
        Q = perimeter - c
        for b in range(1, Q):
            a = Q - b
            triplet = tuple(sorted([a, b, c]))
            if triplet[0] ** 2 + triplet[1] ** 2 == triplet[2] ** 2:
                if triplet not in pyth_trips:
                    pyth_trips.append(triplet)
    return pyth_trips


if __name__ == "__main__":
    maxlen = 0
    maxlen_index = 0
    for j in range(3, 1000):
        z = pythagorean_trips_from_perimeter(j)
        if len(z) > maxlen:
            maxlen_index = j
            maxlen = len(z)

    print(maxlen_index, maxlen)
