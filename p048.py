if __name__ == '__main__':
    z = list(str(sum([j**j for j in range(1, 1001)])))
    last_ten = z[-10:]
    st = ''
    for dig in last_ten:
        st = st + dig

    print(int(st))




