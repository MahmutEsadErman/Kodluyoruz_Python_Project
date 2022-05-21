liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
newListe = []
def flatten(l):

    for i in l:
        if isinstance(i, list):
            flatten(i)
        else:
            newListe.append(i)

    return newListe

print(flatten(liste))
