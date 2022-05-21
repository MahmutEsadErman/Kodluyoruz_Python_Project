liste = [[1, 2], [3, 4], [[5, 6], 7]]


def reverse(l):
    l.reverse()
    for i in l:
        try:
            reverse(i)
        except:
            continue
    return l
print(reverse(liste))
