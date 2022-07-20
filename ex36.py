def remove_duplicatas(lista):
    nova = []
    for i in lista:
        if i not in nova:
            nova.append(i)
    return nova