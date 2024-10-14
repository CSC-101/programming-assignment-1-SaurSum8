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



# Part 4


# Part 5


# Part 6


# Part 7


# Part 8


