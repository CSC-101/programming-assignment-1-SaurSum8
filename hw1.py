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
def rectangle_area(ret: data.Rectangle) -> float:
    LP = ret.top_left
    RP = ret.bottom_right

    l = abs(LP.x - RP.x)
    w = abs(LP.y - RP.y)

    return l * w

# Part 6
def books_by_author(an:str, lb:list[data.Book]) -> list[data.Book]:
    ab = []
    for i in lb:
        if an in i.authors:
            ab.append(i)

    return ab

# Part 7
def circle_bound(ret: data.Rectangle) -> data.Circle:
    cx = (ret.top_left.x + ret.bottom_right.x) / 2
    cy = (ret.top_left.y + ret.bottom_right.y) / 2

    r = ((ret.top_left.x - cx)**2 + ((ret.top_left.y - cy)**2))**(0.5)
    p = data.Point(cx, cy)

    C = data.Circle(p, r)

    return C

# Part 8
def below_pay_average(elist: list[data.Employee]) -> list[str]:
    s = 0
    for i in elist:
        s += i.pay_rate

    if(len(elist) > 0):
        s /= len(elist)
    r = []

    for i in elist:
        if(i.pay_rate < s):
            r.append(i.name)

    return r