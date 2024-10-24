import data

# Write your functions for each part in the space below.

#NOTE TO GRADER: ************************
#This assignment was not completed late
#I just forgot to add comments, you can verify this by
#checking this history of this repository

# Part 1
#Function counts the number of vowels in a given string regardless of capitalization
#Takes string as an input
#Returns integer (count of vowels) as output
def vowel_count(val:str) -> int:
    l = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in val:
        if i.lower() in l:
            count += 1

    return count

# Part 2
#Function takes out nested lists of length 2 from input list, and returns them all,
#contained in a new list
#Takes a list of lists of integers,
#Returns a list of lists of integers (2 integers specifically)
def short_lists(val:list[list[int]]) -> list[list[int]]:
    nList = []

    for i in val:
        if len(i) == 2:
            nList.append(i)

    return nList

# Part 3
#Function takes a list of lists of integers as inputs, and returns the same,
#but all nested lists of length 2 are sorted
#Takes list of lists of integers as input
#Returns list of lists of integers as output
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
#Function adds two Price objects and returns it in proper format
#Takes two Price objects as input
#Returns a Price object as output
def add_prices(priceA: data.Price, priceB: data.Price) -> data.Price:
    nd = priceA.dollars + priceB.dollars
    nc = priceA.cents + priceB.cents
    nd += nc // 100
    nc = nc % 100

    ret = data.Price(nd, nc)
    return ret

# Part 5
#Function calculates the area of a rectangle, based on its top-left and bottom-right points
#Takes a Rectangle object as input
#Returns a float value as output
def rectangle_area(ret: data.Rectangle) -> float:
    LP = ret.top_left
    RP = ret.bottom_right

    l = abs(LP.x - RP.x)
    w = abs(LP.y - RP.y)

    return l * w

# Part 6
#Function, given a list of books and its authors, returns a list of books for a specific,
#given author
#Takes a string (given author's name) and list of Book objects as input
#Returns a list of Book objects as output
def books_by_author(an:str, lb:list[data.Book]) -> list[data.Book]:
    ab = []
    for i in lb:
        if an in i.authors:
            ab.append(i)

    return ab

# Part 7
#Function returns a circle that bounds a given rectangle
#Takes a Rectangle Object as input
#Returns a Circle object as output
def circle_bound(ret: data.Rectangle) -> data.Circle:
    cx = (ret.top_left.x + ret.bottom_right.x) / 2
    cy = (ret.top_left.y + ret.bottom_right.y) / 2

    r = ((ret.top_left.x - cx)**2 + ((ret.top_left.y - cy)**2))**(0.5)
    p = data.Point(cx, cy)

    C = data.Circle(p, r)

    return C

# Part 8
#Function, given a list of Employees, calculates their average pay rate
#then returns the names of employees with pay rate below this average
#Takes a list of Employee object as input
#Returns a list of strings (names of those employees)
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