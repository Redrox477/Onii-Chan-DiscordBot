#Author : Monish Kumar A

from collections import Counter


def r_s(a, b):
    a = a.lower()
    b = b.lower()
    l1 = list(a)
    l2 = list(b)
    l4 = list(b)
    l3 = list(a)
    c = dict(Counter(l3))
    d = dict(Counter(l4))
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                e = l1[i]
                j = l1.index(e)
                if j == 0:
                    if c[e] == d[e]:
                        l3.remove(e)
                        l4.remove(e)
                        c[e] = c[e] - 1
                        d[e] = d[e] - 1
                        break
                    elif c[e] > 1 and d[e] == 1:
                        l3.remove(e)
                        l4.remove(e)
                        c[e] = c[e] - 1
                        d[e] = d[e] - 1
                    elif c[e] == 1 and d[e] > 1:
                        l3.remove(e)
                        l4.remove(e)
                        d[e] = d[e] - 1
                        c[e] = c[e] - 1
                    elif c[e] > 1 and d[e] > 1:
                        if c[e] > d[e]:
                            l3.remove(e)
                            l4.remove(e)
                            c[e] = c[e] - 1
                            d[e] = d[e] - 1
                        elif d[e] > c[e]:
                            l3.remove(e)
                            l4.remove(e)
                            d[e] = d[e] - 1
                            c[e] = c[e] - 1
                        else:
                            break
                else:
                    for o in range(j):
                        if e == l1[o]:
                            break
                        else:
                            if c[e] == d[e]:
                                if c[e] == 0 and [e] == 0:
                                    break
                                elif c[e] > 0 and d[e] > 0:
                                    l3.remove(e)
                                    l4.remove(e)
                                    c[e] = c[e] - 1
                                    d[e] = d[e] - 1
                            elif c[e] > 1 and d[e] == 1:
                                l3.remove(e)
                                l4.remove(e)
                                c[e] = c[e] - 1
                                d[e] = d[e] - 1
                            elif c[e] == 1 and d[e] > 1:
                                l3.remove(e)
                                l4.remove(e)
                                d[e] = d[e] - 1
                                c[e] = c[e] - 1
                            elif c[e] > 1 and d[e] > 1:
                                if c[e] > d[e]:
                                    l3.remove(e)
                                    l4.remove(e)
                                    c[e] = c[e] - 1
                                    d[e] = d[e] - 1
                                else:
                                    l3.remove(e)
                                    l4.remove(e)
                                    d[e] = d[e] - 1
                                    c[e] = c[e] - 1
    w = l3 + l4 + [' ']
    k = dict(Counter(w))
    k1 = w
    r = ' '
    while k[r] > 0:
        k1.remove(r)
        k[r] -= 1
        if k[r] == 0:
            break
        else:
            continue
    n = len(k1)
    result = ["FRIENDS", "LOVE", "AFFECTION", "MARRIAGE", "ENEMY", "SISTER"]
    while len(result) > 1:
        m = n % len(result) - 1
        if m >= 0:
            right = result[m + 1:]
            left = result[:m]
            result = right + left
        else:
            result = result[:len(result) - 1]
    if result[0] == 'ENEMY':
        res = 'RELATIONSHIP STATUS : ' + result[
            0] + ', you two are not made for each other :('

    else:
        res = 'RELATIONSHIP STATUS : ' + result[0]

    return res
