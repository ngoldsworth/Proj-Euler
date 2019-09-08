import inflect

def numwords(num):
    z = inflect.engine().number_to_words(num)
    return z

def remove_bads(num_as_word):
    first = num_as_word.replace(' ', '')
    second = num_as_word.replace('-', '')
    return second

def letters_in_number_as_word(num: int):
    q = numwords(num)
    r = remove_bads(q)
    s = len(r)
    return s

grand_tot = 0
for i in range(1, 1001):
    w = letters_in_number_as_word(i)
    grand_tot += w

print(grand_tot)
