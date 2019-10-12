from itertools import permutations as permus


def unused_digits(already_used_digits: list):
    return [i for i in list(range(0,10)) if i not in already_used_digits]


def diglist_to_int(list_of_digits: list):
    if len(list_of_digits) == 0:
        return None
    else:
        numstr = ''
        for d in list_of_digits:
            numstr = numstr + str(d)
        return int(numstr)

def next_digits( digitlist, modular_list, modj, list_to_put_results_in):
    '''

    :param digitlist: List of digits already made.
    :param modular_list: list of mod checks, for checking divisibility
    :param modj: index of the mod list currently on
    :param list_to_put_results_in: name of a list to put all results into, must bne initialized outside of this function
    :return:
    '''

    if len(digitlist) == 10:
        list_to_put_results_in.append(diglist_to_int(digitlist))

    elif diglist_to_int(digitlist[-3:]) % modular_list[modj] == 0:
        remaining = unused_digits(digitlist)
        for newdig in remaining:
            new_digitlist = digitlist + [newdig]
            next_digits(new_digitlist, modular_list, modj+1, list_to_put_results_in)

if __name__ == '__main__':
    first_perm_set = permus(list(range(0, 10)), 3)
    satisfactorty_list = []
    modlist = [1, 2, 3, 5, 7, 11, 13, 17, 19]
    for perm in first_perm_set:
        trip = list(perm)
        # if diglist_to_int(quadrup[-3:]) % 2 == 0:
        #     rem4 = unused_digits(quadrup)
        #     for d5 in rem4:
        #         pentup = quadrup + [d5]
        #         if diglist_to_int(pentup[-3:]) % 3 == 0:
        #             rem5 = unused_digits(pentup)
        #             for d6 in rem5:
        #                 hexup = pentup + [d6]
        #                 if diglist_to_int(hexup[-3:]) % 5 == 0:
        #                     rem6 = unused_digits(hexup)
        #                     for d7 in rem6:
        #                         septup = hexup + [d7]
        #                         if diglist_to_int(septup[-3:]) % 7 == 0:
        #                             rem7 = unused_digits(septup)
        #                             for d8 in rem7:
        #                                 octup = septup + [d8]
        #                                 if diglist_to_int(octup[-3:]) % 11 == 0:
        #                                     rem8 = unused_digits(octup)
        #                                     for d9 in rem8:
        #                                         nonup = octup + [d9]
        #                                         if diglist_to_int(nonup[-3:]) % 13 == 0:
        #                                             rem9 = unused_digits(nonup)
        #                                             for d10 in rem9:
        #                                                 decatup = nonup + [d10]
        #                                                 if diglist_to_int(decatup[-3:]) % 17 == 0:
        #                                                     satisfactorty_list.append(diglist_to_int(decatup))
        next_digits(trip, modlist, 0, satisfactorty_list)
    print(satisfactorty_list)
    print(sum(satisfactorty_list))
