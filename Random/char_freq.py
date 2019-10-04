def possibleSameCharFreqByOneRemoval(s):
    lst = [0] * 128
    for i in s:
        lst[ord(i)] += 1
    same = 0
    flag = 1
    for i in range(0, 128):
        if lst[i] > 0:
            same = lst[i]
            break
    for j in range(i + 1, 128):
        if lst[j] > 0 and lst[j] != same:
            flag = 0
    if flag == 1:
        return lst[i]
    for i in range(128):
        if lst[i] >= 1:
            lst[i] -= 1
            same = 0
            flag = 1
            for j in range(0, 128):
                if lst[j] > 0:
                    same = lst[j]
                    break
            for k in range(j + 1, 128):
                if lst[k] > 0 and lst[k] != same:
                    flag = 0
                    break
            if flag == 1:
                return lst[j]
            lst[i] += 1
    return 0


if __name__ == "__main__":
    str1 = "MADAMAMAMAMAMDDDDDD"
    if (possibleSameCharFreqByOneRemoval(str1)):
        print(possibleSameCharFreqByOneRemoval(str1))
    else:
        print(0)
