import data

# Write your functions for each part in the space below.

# Part 1
def vowel_count(val:str) -> int:
    l = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in val:
        if i.lower() in l:
            count += 1

    return count

# Part 2
def short_lists(val:list[list[int]]) -> list[list[int]]:
    nList = []

    for i in val:
        if len(i) == 2:
            nList.append(i)

    return nList

# Part 3
def ascending_pairs(inpList: list[list[int]]) -> list[list[int]]:

    ret = []

    for i in inpList:
        if len(i) == 2:
            t = [i[0], i[1]]
            t.sort()
            ret.append(t)
        else:
            ret.append(i)

    return ret



# Part 4
def add_prices(priceA: data.Price, priceB: data.Price) -> data.Price:
    nd = priceA.dollars + priceB.dollars
    nc = priceA.cents + priceB.cents
    nd += nc // 100
    nc = nc % 100

    ret = data.Price(nd, nc)
    return ret

# Part 5

# Part 6


# Part 7


# Part 8


