def triangular(n):
    return int(n*(n+1)/2)


def wordscore(word: str):
    return sum([(ord(char) - 96) for char in word.lower()])


# def check_score_in_list(n: int, list_to_check: list):
#     if n in list_to_check:
#         return True
#     else:
#         return False

if __name__ == '__main__':
    wl = open('p042_words.txt', 'r').read().split(',')
    tri_list = [triangular(i) for i in range(25)]

    score_list = []
    count = 0
    for word in wl:
        z = wordscore(word)
        score_list.append(z)
        if z in tri_list:
            count += 1

    print(count)
