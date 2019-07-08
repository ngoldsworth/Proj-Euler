from p021 import divlist as dl

def pandigit_ids(num: int):
    """
    Checks if input number has pandigit identity
    :param num: input number
    :return: list of all numbers (including num) that have pandigit identity with num
    """
    divlist = dl(num)
    pandigit_list = []
    for dvsr in divlist:
        quotient = num / dvsr
        alist = list(str(int(dvsr)))
        blist = list(str(int(quotient)))
        prodlist = list(str(num))

        if len(alist) == len(set(alist)) and len(blist) == len(set(blist)) and len(prodlist) == len(set(prodlist)):
            checklist = prodlist + alist + blist
            if len(checklist) == len(set(checklist)):
                print(dvsr, quotient)
                if not any(i in alist for i in blist):
                    checklist = alist + blist + prodlist
                    checklist = [int(num) for num in checklist]
                    checklist.sort()
                    if checklist == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                        pandigit_list.append(num)
                        pandigit_list.append(quotient)
                        pandigit_list.append(dvsr)
    pandigit_list = list(set(pandigit_list))
    return pandigit_list

panlist = []
for num in range(987654321):
    panlist.extend(pandigit_ids(num))

print(panlist)
