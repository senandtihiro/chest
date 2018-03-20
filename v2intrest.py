def get_elements(s):
    q = []
    while len(s) != 1:
        q.append(s[0])
        s = s[1]
    q.append(s)

    return q


def nested_list(l):
    res = ()
    ele0 = l[0]
    res += (ele0, )
    l.remove(ele0)
    if len(l) > 0:
        res += ((nested_list(l), ))

    return res


def main():
    s = ('a', ('b', ('c', ('d', ('e', ('f'))))))
    l = get_elements(s)
    l = l[::-1]
    ll = nested_list(l)
    print(ll)


if __name__ == '__main__':
    main()